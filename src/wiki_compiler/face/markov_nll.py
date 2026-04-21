"""
Markov Chain NLL - Alternativa simple a LLM para calcular entropía.
Entrena un modelo n-gram sobre el corpus y calcula NLL por token.
"""

import re
from collections import Counter, defaultdict
from typing import Dict, List, Tuple
import numpy as np
from dataclasses import dataclass


@dataclass
class MarkovModel:
    """N-gram language model basado en Markov chains."""

    order: int
    ngram_counts: Dict[Tuple[str, ...], Counter]
    context_counts: Dict[Tuple[str, ...], int]
    vocab: set
    smoothing: float = 1e-6

    def prob(self, token: str, context: Tuple[str, ...]) -> float:
        """P(token | context) con Laplace smoothing."""
        if token not in self.vocab:
            token = "<UNK>"

        ngram = context + (token,)
        count = self.ngram_counts.get(context, Counter()).get(token, 0)
        total = self.context_counts.get(context, 0)

        if total == 0:
            return 1.0 / (len(self.vocab) + 1)

        return (count + self.smoothing) / (total + self.smoothing * len(self.vocab))

    def nll(self, token: str, context: Tuple[str, ...]) -> float:
        """Negative log likelihood: -log P(token | context)"""
        p = self.prob(token, context)
        return -np.log(p + 1e-10)


def tokenize(text: str) -> List[str]:
    """Tokenización simple: palabras o caracteres."""
    return re.findall(r"\b\w+\b|[^\w\s]|\s+", text.lower())


def train_markov(texts: List[str], order: int = 2) -> MarkovModel:
    """Entrena un modelo Markov sobre los textos."""
    ngram_counts = defaultdict(Counter)
    context_counts = Counter()
    vocab = set()

    for text in texts:
        tokens = tokenize(text)
        vocab.update(tokens)

        for i in range(len(tokens) - order):
            context = tuple(tokens[i : i + order])
            token = tokens[i + order]

            ngram_counts[context][token] += 1
            context_counts[context] += 1

    vocab.add("<UNK>")

    return MarkovModel(
        order=order,
        ngram_counts=dict(ngram_counts),
        context_counts=dict(context_counts),
        vocab=vocab,
    )


def compute_nll_sequence(text: str, model: MarkovModel) -> np.ndarray:
    """Calcula la secuencia de NLLs para un texto."""
    tokens = tokenize(text)
    nlls = []

    # Usar los primeros 'order' tokens como contexto inicial
    for i in range(model.order, len(tokens)):
        context = tuple(tokens[i - model.order : i])
        token = tokens[i]
        nll = model.nll(token, context)
        nlls.append(nll)

    return np.array(nlls)


class MarkovFaceAnalyzer:
    """FACE analyzer usando Markov chains en lugar de LLM."""

    def __init__(self, order: int = 2, preprocess: str = "zscore"):
        from src.wiki_compiler.face import FFTProcessor, SpectrumComparator

        self.order = order
        self.fft = FFTProcessor(preprocess)
        self.comparator = SpectrumComparator()
        self.model = None

    def train(self, texts: List[str]):
        """Entrena el modelo Markov sobre los textos."""
        self.model = train_markov(texts, self.order)
        print(
            f"Markov model trained: vocab={len(self.model.vocab)}, contexts={len(self.model.context_counts)}"
        )

    def compute_nll(self, text: str) -> np.ndarray:
        """Calcula NLL sequence para un texto."""
        if self.model is None:
            raise ValueError("Model not trained. Call train() first.")
        return compute_nll_sequence(text, self.model)

    def analyze_text(self, text: str) -> Tuple[np.ndarray, np.ndarray]:
        """FFT del texto (usa NLL de Markov)."""
        nll_seq = self.compute_nll(text)
        return self.fft.compute_fft(nll_seq)

    def analyze_texts(self, texts: List[str]) -> List[Tuple[np.ndarray, np.ndarray]]:
        """FFT de múltiples textos."""
        results = []
        for text in texts:
            try:
                results.append(self.analyze_text(text))
            except:
                results.append((np.array([]), np.array([])))
        return results


if __name__ == "__main__":
    from pathlib import Path

    # Cargar textos del proyecto
    code_files = [f for f in Path("src").rglob("*.py") if "__pycache__" not in str(f)]
    texts = [f.read_text() for f in code_files[:50]]

    print(f"Training on {len(texts)} files...")

    # Entrenar modelo de Markov (bigramas)
    model = train_markov(texts, order=2)
    print(f"Model: vocab={len(model.vocab)}, contexts={len(model.context_counts)}")

    # Probar con código limpio vs spaghetti
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
        tmp=result
        for j in range(5):
            result=result+tmp
            if j==3:
                for k in range(10):
                    result+=k
    return result
"""

    nll_clean = compute_nll_sequence(clean, model)
    nll_spaghetti = compute_nll_sequence(spaghetti, model)

    print(
        f"\nClean NLL stats: mean={np.mean(nll_clean):.2f}, std={np.std(nll_clean):.2f}"
    )
    print(
        f"Spaghetti NLL stats: mean={np.mean(nll_spaghetti):.2f}, std={np.std(nll_spaghetti):.2f}"
    )

    # FFT
    from src.wiki_compiler.face import FaceAnalyzer

    fft_analyzer = FaceAnalyzer(preprocess="zscore")
    spec_clean = fft_analyzer.fft.compute_fft(nll_clean)
    spec_spaghetti = fft_analyzer.fft.compute_fft(nll_spaghetti)

    m = fft_analyzer.comparator.compare(
        spec_clean[0], spec_clean[1], spec_spaghetti[0], spec_spaghetti[1]
    )
    print(f"\nClean vs Spaghetti (NLL-based FFT):")
    print(f"  SO={m.so:.3f}, CORR={m.corr:.3f}, SAM={m.sam:.3f}")
