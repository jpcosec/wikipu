"""
Markov Chain NLL usando NLTK (API nativa)

Calcula entropía de texto usando n-gram language models de NLTK.
"""

import re
from typing import List, Optional, Dict
from pathlib import Path
import numpy as np
from collections import Counter, defaultdict


class SimpleNGramModel:
    """
    N-gram language model simple sin dependencias externas.

    Implementación propia que usa counters - más transparente que NLTK.
    """

    def __init__(self, order: int = 2, smoothing: float = 1e-6):
        self.order = order
        self.smoothing = smoothing
        self.ngram_counts: Dict[tuple, Counter] = {}
        self.context_counts: Dict[tuple, int] = {}
        self.vocab: set = set()

    def train(self, texts: List[str]) -> "SimpleNGramModel":
        """Entrena el modelo sobre textos."""
        self.ngram_counts = defaultdict(Counter)
        self.context_counts = Counter()
        self.vocab = set()

        for text in texts:
            tokens = self._tokenize(text)
            self.vocab.update(tokens)

            for i in range(len(tokens) - self.order):
                context = tuple(tokens[i : i + self.order])
                token = tokens[i + self.order]
                self.ngram_counts[context][token] += 1
                self.context_counts[context] += 1

        return self

    def _tokenize(self, text: str) -> List[str]:
        """Tokenización simple."""
        return re.findall(r"\b\w+\b", text.lower()) + ["<EOS>"]

    def prob(self, token: str, context: tuple) -> float:
        """P(token | context) con Laplace smoothing."""
        count = self.ngram_counts.get(context, Counter()).get(token, 0)
        total = self.context_counts.get(context, 0)
        vocab_size = len(self.vocab) + 1

        return (count + self.smoothing) / (total + self.smoothing * vocab_size)

    def score(self, token: str, context: tuple) -> float:
        """Alias de prob para compatibilidad."""
        return self.prob(token, context)

    def nll(self, token: str, context: tuple) -> float:
        """-log P(token | context)."""
        p = self.prob(token, context)
        return -np.log(p + 1e-10)

    def logscore(self, token: str, context: tuple) -> float:
        """Log probability."""
        p = self.prob(token, context)
        return np.log(p + 1e-10) if p > 0 else -float("inf")

    def entropy(self, text: str) -> float:
        """Entropía por token del texto."""
        tokens = self._tokenize(text)
        entropies = []

        for i in range(self.order, len(tokens)):
            context = tuple(tokens[i - self.order : i])
            token = tokens[i]
            p = self.prob(token, context)
            if p > 0:
                entropies.append(-np.log2(p))

        return np.mean(entropies) if entropies else 0.0

    def perplexity(self, text: float) -> float:
        """Perplejidad del texto."""
        h = self.entropy(text)
        return 2**h if h > 0 else float("inf")


class NGramEntropy:
    """
    Interfaz unified para calcular entropía de texto con N-grams.

    Uso:
        ne = NGramEntropy(order=2)
        ne.train(texts)  # Entrena sobre corpus
        nlls = ne.nll_sequence("tu texto...")  # NLLs por token
    """

    def __init__(self, order: int = 2, smoothing: float = 1e-6):
        self.order = order
        self.smoothing = smoothing
        self.model: Optional[SimpleNGramModel] = None

    def train(self, texts: List[str]) -> "NGramEntropy":
        """Entrena el modelo N-gram."""
        self.model = SimpleNGramModel(order=self.order, smoothing=self.smoothing)
        self.model.train(texts)
        return self

    def train_from_dir(
        self, path: str, extensions: tuple = (".py", ".md", ".txt")
    ) -> "NGramEntropy":
        """Entrena desde directorio."""
        p = Path(path)
        texts = []

        for ext in extensions:
            for f in p.rglob(f"*{ext}"):
                try:
                    texts.append(f.read_text(encoding="utf-8"))
                except:
                    pass

        return self.train(texts)

    def nll_sequence(self, text: str) -> np.ndarray:
        """Secuencia de NLLs por token."""
        if self.model is None:
            raise ValueError("Model not trained")

        tokens = self.model._tokenize(text)
        nlls = []

        for i in range(self.order, len(tokens)):
            context = tuple(tokens[i - self.order : i])
            token = tokens[i]
            nll = self.model.nll(token, context)
            nlls.append(nll)

        return np.array(nlls)

    def nll_stats(self, text: str) -> Dict:
        """Estadísticas de NLL."""
        nlls = self.nll_sequence(text)

        if len(nlls) == 0:
            return {
                "mean": 0,
                "std": 0,
                "max": 0,
                "min": 0,
                "entropy": 0,
                "perplexity": 0,
            }

        entropy = float(np.mean(nlls))

        return {
            "mean": float(np.mean(nlls)),
            "std": float(np.std(nlls)),
            "max": float(np.max(nlls)),
            "min": float(np.min(nlls)),
            "entropy": entropy,
            "perplexity": float(np.exp(entropy)),
            "token_count": len(nlls),
        }

    def batch_nll(self, texts: List[str]) -> List[np.ndarray]:
        """NLL para múltiples textos."""
        return [self.nll_sequence(t) for t in texts]

    def batch_stats(self, texts: List[str]) -> List[Dict]:
        """Estadísticas para múltiples textos."""
        return [self.nll_stats(t) for t in texts]


class CategoryClassifier:
    """Clasificador basado en N-gram entropy."""

    def __init__(self, order: int = 2, smoothing: float = 1e-6):
        self.order = order
        self.smoothing = smoothing
        self.category_models: Dict[str, NGramEntropy] = {}

    def train_category(self, name: str, texts: List[str]) -> "CategoryClassifier":
        """Entrena una categoría."""
        model = NGramEntropy(order=self.order, smoothing=self.smoothing)
        model.train(texts)
        self.category_models[name] = model
        return self

    def classify(self, text: str) -> Dict:
        """Clasifica un texto en categorías."""
        if not self.category_models:
            raise ValueError("No categories trained")

        entropies = {}
        for name, model in self.category_models.items():
            try:
                stats = model.nll_stats(text)
                entropies[name] = stats["entropy"]
            except:
                entropies[name] = float("inf")

        if not entropies:
            return {"category": None, "scores": {}}

        best = min(entropies, key=entropies.get)
        total = sum(1 / (v + 0.1) for v in entropies.values())
        scores = {k: (1 / (v + 0.1)) / total for k, v in entropies.items()}

        return {
            "category": best,
            "scores": scores,
            "entropy": entropies,
        }

    def compare(self, text1: str, text2: str) -> Dict:
        """Compara dos textos."""
        first = next(iter(self.category_models.values()))
        s1 = first.nll_stats(text1)
        s2 = first.nll_stats(text2)

        return {
            "text1_entropy": s1["entropy"],
            "text2_entropy": s2["entropy"],
            "diff": abs(s1["entropy"] - s2["entropy"]),
            "ratio": s1["entropy"] / (s2["entropy"] + 0.01),
        }


def demo():
    """Demo básica."""
    from pathlib import Path

    # Cargar código
    code_files = [f for f in Path("src").rglob("*.py") if "__pycache__" not in str(f)][
        :30
    ]
    texts = [f.read_text() for f in code_files]

    # Entrenar
    ne = NGramEntropy(order=2)
    ne.train(texts)
    print(
        f"Modelo entrenado: vocab={len(ne.model.vocab)}, contexts={len(ne.model.context_counts)}"
    )

    # Test
    clean = "def calculate_fibonacci(n):\n    if n <= 1:\n        return n\n    a, b = 0, 1\n    for _ in range(2, n + 1):\n        a, b = b, a + b\n    return b"

    spaghetti = "def doStuff(x):\n    result=0\n    if x>10:\n        for i in range(x):\n            if i%2==0:result=result+i\n    return result"

    print(f"Clean entropy: {ne.nll_stats(clean)['entropy']:.2f}")
    print(f"Spaghetti entropy: {ne.nll_stats(spaghetti)['entropy']:.2f}")


if __name__ == "__main__":
    demo()
