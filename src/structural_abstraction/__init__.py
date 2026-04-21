"""
Structural Abstraction Analyzer

Mide estructura de código a nivel de abstracción (funciones, clases, patrones)
en vez de tokens individuales.
"""

import ast
import re
from typing import List, Dict, Set, Optional, Tuple
from dataclasses import dataclass
import numpy as np
from collections import Counter


@dataclass
class FunctionSignature:
    """Representación abstracta de una función."""

    name: str
    params: List[str]
    returns: Optional[str]
    complexity: int  # número de statements
    nested_depth: int
    calls: List[str]  # funciones que llama


@dataclass
class ClassStructure:
    """Representación abstracta de una clase."""

    name: str
    methods: List[FunctionSignature]
    attributes: List[str]
    inheritance: List[str]


class StructuralParser:
    """
    Extrae estructura a nivel de abstracción desde código Python.

    En vez de tokens, mide:
    - Firmas de funciones: function(param1, param2, ...)
    - Clases y métodos
    - Patrones de control (if/for/while anidados)
    - Llamadas a funciones
    """

    def __init__(self):
        self.functions: List[FunctionSignature] = []
        self.classes: List[ClassStructure] = []
        self._current_class = None

    def parse(self, code: str) -> Tuple[List[FunctionSignature], List[ClassStructure]]:
        """Parse código y extrae estructuras."""
        try:
            tree = ast.parse(code)
        except:
            return [], []

        self.functions = []
        self.classes = []
        self._current_class = None

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                self._parse_class(node)
            elif isinstance(node, ast.FunctionDef):
                self._parse_function(node)

        return self.functions, self.classes

    def _parse_class(self, node: ast.ClassDef):
        """Parse una clase."""
        methods = []
        for item in node.body:
            if isinstance(item, ast.FunctionDef):
                methods.append(self._parse_function(item, in_class=True))

        attrs = []
        for item in node.body:
            if isinstance(item, ast.Assign):
                for target in item.targets:
                    if isinstance(target, ast.Name):
                        attrs.append(target.id)

        inheritance = [n.id for n in node.bases if isinstance(n, ast.Name)]

        self.classes.append(
            ClassStructure(
                name=node.name,
                methods=methods,
                attributes=attrs,
                inheritance=inheritance,
            )
        )

    def _parse_function(
        self, node: ast.FunctionDef, in_class: bool = False
    ) -> FunctionSignature:
        """Parse una función."""
        params = [arg.arg for arg in node.args.args]

        # Returns
        returns = None
        if node.returns and isinstance(node.returns, ast.Name):
            returns = node.returns.id

        # Complexity (simple count)
        complexity = sum(
            1
            for _ in ast.walk(node)
            if isinstance(_, (ast.If, ast.For, ast.While, ast.Try))
        )

        # Nested depth
        nested_depth = self._get_nesting_depth(node)

        # Function calls
        calls = []
        for child in ast.walk(node):
            if isinstance(child, ast.Call):
                if isinstance(child.func, ast.Name):
                    calls.append(child.func.id)
                elif isinstance(child.func, ast.Attribute):
                    calls.append(child.func.attr)

        sig = FunctionSignature(
            name=node.name,
            params=params,
            returns=returns,
            complexity=complexity,
            nested_depth=nested_depth,
            calls=list(set(calls)),
        )

        if not in_class:
            self.functions.append(sig)

        return sig

    def _get_nesting_depth(self, node: ast.AST) -> int:
        """Calcula profundidad máxima de anidación."""

        def depth(n: ast.AST, d: int = 0) -> int:
            max_d = d
            for child in ast.iter_child_nodes(n):
                if isinstance(
                    child,
                    (ast.If, ast.For, ast.While, ast.With, ast.Try, ast.FunctionDef),
                ):
                    max_d = max(max_d, depth(child, d + 1))
            return max_d

        return depth(node)


def signature_to_sequence(sig: FunctionSignature) -> List[str]:
    """Convierte firma a secuencia de símbolos para FFT."""
    seq = [f"FUNC_{sig.name}"]
    seq.extend([f"ARG_{p}" for p in sig.params])
    if sig.returns:
        seq.append(f"RET_{sig.returns}")
    seq.extend([f"CALL_{c}" for c in sig.calls])
    seq.append(f"DEPTH_{sig.nested_depth}")
    seq.append(f"COMPLEX_{sig.complexity}")
    return seq


def class_to_sequence(cls: ClassStructure) -> List[str]:
    """Convierte clase a secuencia."""
    seq = [f"CLASS_{cls.name}"]
    seq.extend([f"INHERIT_{i}" for i in cls.inheritance])
    seq.extend([f"ATTR_{a}" for a in cls.attributes])
    for method in cls.methods:
        seq.extend(signature_to_sequence(method))
    return seq


def code_to_structural_sequence(code: str) -> List[str]:
    """Convierte código completo a secuencia de estructuras."""
    parser = StructuralParser()
    funcs, classes = parser.parse(code)

    seq = []

    # Agregar funciones
    for func in funcs:
        seq.extend(signature_to_sequence(func))

    # Agregar clases
    for cls in classes:
        seq.extend(class_to_sequence(cls))

    return seq


class StructuralEntropy:
    """
    Mide entropía a nivel de estructura (funciones, clases).

    En vez de tokens individuales, mide patrones como:
    - "function(arg1, arg2)"
    - "class inherits from X"
    - "function calls A, calls B"
    """

    def __init__(self, n_gram: int = 2):
        self.n_gram = n_gram
        self.ngram_counts = {}
        self.context_counts = {}
        self.vocab = set()

    def train(self, texts: List[str]):
        """Entrena sobre secuencias estructurales."""
        self.ngram_counts = {}
        self.context_counts = {}
        self.vocab = set()

        for text in texts:
            # Extraer estructura del código
            seq = code_to_structural_sequence(text)
            self.vocab.update(seq)

            # N-grams
            for i in range(len(seq) - self.n_gram):
                context = tuple(seq[i : i + self.n_gram])
                token = seq[i + self.n_gram]

                if context not in self.ngram_counts:
                    self.ngram_counts[context] = Counter()

                self.ngram_counts[context][token] += 1
                self.context_counts[context] = self.context_counts.get(context, 0) + 1

    def entropy(self, code: str) -> float:
        """Calcula entropía estructural del código."""
        seq = code_to_structural_sequence(code)

        if len(seq) < self.n_gram:
            return 0.0

        entropies = []
        for i in range(self.n_gram, len(seq)):
            context = tuple(seq[i - self.n_gram : i])
            token = seq[i]

            # Smooth: si no existe el contexto, usar distribución uniforme
            total = self.context_counts.get(context, 0)

            if total == 0:
                # Contexto no visto - alta incertidumbre
                p = 1.0 / (len(self.vocab) + 1)
            else:
                count = self.ngram_counts.get(context, Counter()).get(token, 0)
                p = (count + 1e-6) / (total + 1e-6 * len(self.vocab))

            entropies.append(-np.log2(p + 1e-10))

        return np.mean(entropies) if entropies else 0.0


def demo():
    """Demo básica."""
    from pathlib import Path

    # Código de ejemplo
    clean = """
def calculate_fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
"""

    spaghetti = """
def doStuff(x):
    result=0
    if x>10:
        for i in range(x):
            if i%2==0:
                result=result+i
                if result>100:
                    break
    else:
        result=x*2
    return result
"""

    print("=== Structural Parsing ===")

    parser = StructuralParser()
    funcs1, classes1 = parser.parse(clean)
    funcs2, classes2 = parser.parse(spaghetti)

    print(f"Clean: {len(funcs1)} functions, {len(classes1)} classes")
    print(f"Spaghetti: {len(funcs2)} functions, {len(classes2)} classes")

    # Secuencias estructurales
    seq1 = code_to_structural_sequence(clean)
    seq2 = code_to_structural_sequence(spaghetti)

    print(f"\nStructural sequence clean (first 20): {seq1[:20]}")
    print(f"Structural sequence spaghetti (first 20): {seq2[:20]}")

    # Entrenar y calcular entropía
    print("\n=== Structural Entropy ===")
    se = StructuralEntropy(n_gram=2)

    # Cargar código real
    code_files = [f for f in Path("src").rglob("*.py") if "__pycache__" not in str(f)][
        :30
    ]
    texts = [f.read_text() for f in code_files]

    se.train(texts)
    print(f"Vocab size: {len(se.vocab)}")

    print(f"Clean entropy: {se.entropy(clean):.2f}")
    print(f"Spaghetti entropy: {se.entropy(spaghetti):.2f}")


if __name__ == "__main__":
    demo()
