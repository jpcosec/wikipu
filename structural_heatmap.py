"""
Structural Metrics Heatmap

Genera un heatmap de similitud estructural entre todos los archivos del proyecto.
Usa: FFT(Markov(Structure(Code)))

Usage:
    python structural_heatmap.py [--output output.png]
"""

import argparse
import sys
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.spatial.distance import pdist, squareform

sys.path.insert(0, ".")

from src.structural_abstraction import code_to_structural_sequence
from src.markov_entropy import NGramEntropy
from src.wiki_compiler.face import FaceAnalyzer


def analyze_project(
    root: Path = Path("."),
    include_patterns: list = None,
    exclude_patterns: list = None,
) -> dict:
    """Analiza todos los archivos y retorna métricas."""

    if include_patterns is None:
        include_patterns = ["*.py"]
    if exclude_patterns is None:
        exclude_patterns = ["__pycache__", "venv", ".git"]

    files = []
    for pattern in include_patterns:
        files.extend(root.rglob(pattern))

    # Filter
    filtered = []
    for f in files:
        exclude = any(ex in str(f) for ex in exclude_patterns)
        if not exclude:
            try:
                if len(f.read_text()) > 100:
                    filtered.append(f)
            except:
                pass

    # Entrenar modelo
    print(f"Training on {len(filtered[:50])} files...")
    texts = [f.read_text() for f in filtered[:50]]
    structural_texts = [" ".join(code_to_structural_sequence(t)) for t in texts]

    ne = NGramEntropy(order=2)
    ne.train(structural_texts)

    analyzer = FaceAnalyzer(preprocess="zscore")

    # Calcular espectro para cada archivo
    results = []
    for f in filtered:
        try:
            code = f.read_text()
            seq = " ".join(code_to_structural_sequence(code))
            nll = ne.nll_sequence(seq)
            freq, power = analyzer.fft.compute_fft(nll)

            results.append(
                {
                    "file": f.name,
                    "path": str(f),
                    "freq": freq,
                    "power": power,
                    "nll_mean": np.mean(nll) if len(nll) > 0 else 0,
                    "nll_std": np.std(nll) if len(nll) > 0 else 0,
                }
            )
        except Exception as e:
            print(f"Error {f}: {e}")

    return results


def compute_similarity_matrix(results: list, analyzer: FaceAnalyzer) -> np.ndarray:
    """Computa matriz de similitud (SO) entre todos los archivos."""
    n = len(results)
    matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(i, n):
            if i == j:
                matrix[i, j] = 1.0
            else:
                try:
                    m = analyzer.comparator.compare(
                        results[i]["freq"],
                        results[i]["power"],
                        results[j]["freq"],
                        results[j]["power"],
                    )
                    matrix[i, j] = m.so
                    matrix[j, i] = m.so
                except:
                    matrix[i, j] = 0
                    matrix[j, i] = 0

    return matrix


def plot_heatmap(
    results: list,
    matrix: np.ndarray,
    output: str = None,
    title: str = "Structural Similarity Heatmap",
):
    """Genera y guarda el heatmap."""

    # Reducir nombres de archivos para display
    names = [r["file"][:20] for r in results]

    # Truncar matrix si es muy grande
    if len(names) > 50:
        print(f"Showing first 50 of {len(names)} files")
        names = names[:50]
        matrix = matrix[:50, :50]

    # Plot
    fig, ax = plt.subplots(figsize=(14, 12))

    sns.heatmap(
        matrix,
        xticklabels=names,
        yticklabels=names,
        cmap="RdYlGn",
        vmin=0,
        vmax=1,
        annot=False,
        square=True,
        cbar_kws={"label": "Spectral Overlap"},
        ax=ax,
    )

    plt.xticks(rotation=90, fontsize=8)
    plt.yticks(rotation=0, fontsize=8)
    plt.title(title, fontsize=14)
    plt.tight_layout()

    if output:
        plt.savefig(output, dpi=150)
        print(f"Heatmap saved to {output}")
    else:
        plt.show()


def plot_dendrogram(
    results: list,
    matrix: np.ndarray,
    output: str = None,
):
    """Genera dendrograma de clustering."""
    from scipy.cluster.hierarchy import linkage, dendrogram

    # Convertir similitud a distancia
    dist_matrix = 1 - matrix

    # Clustering
    linkage_matrix = linkage(squareform(dist_matrix), method="average")

    fig, ax = plt.subplots(figsize=(14, 8))

    names = [r["file"][:15] for r in results[:50]]

    dendrogram(
        linkage_matrix,
        labels=names,
        leaf_rotation=90,
        leaf_font_size=8,
        ax=ax,
    )

    plt.title("Structural Clustering (Hierarchical)")
    plt.xlabel("Files")
    plt.ylabel("Distance")
    plt.tight_layout()

    if output:
        plt.savefig(output, dpi=150)
        print(f"Dendrogram saved to {output}")
    else:
        plt.show()


def main():
    parser = argparse.ArgumentParser(description="Structural Metrics Heatmap")
    parser.add_argument(
        "--output", "-o", type=str, default=None, help="Output image path"
    )
    parser.add_argument(
        "--type",
        "-t",
        type=str,
        default="heatmap",
        choices=["heatmap", "dendrogram", "both"],
    )
    parser.add_argument("--root", "-r", type=str, default="src", help="Root directory")
    args = parser.parse_args()

    root = Path(args.root)
    print(f"Analyzing {root}...")

    # Analizar
    results = analyze_project(root)
    print(f"Analyzed {len(results)} files")

    if not results:
        print("No files found")
        return

    # Matriz de similitud
    analyzer = FaceAnalyzer(preprocess="zscore")
    matrix = compute_similarity_matrix(results, analyzer)

    # Plots
    if args.type in ["heatmap", "both"]:
        output_heat = args.output or "structural_heatmap.png"
        plot_heatmap(results, matrix, output_heat)

    if args.type in ["dendrogram", "both"]:
        output_dend = (
            args.output.replace(".png", "_dendrogram.png")
            if args.output
            else "structural_dendrogram.png"
        )
        plot_dendrogram(results, matrix, output_dend)

    # Stats
    print("\n=== Estructura del Proyecto ===")
    print(f"Total archivos: {len(results)}")

    # Archivos más distintos al promedio
    avg_similarities = matrix.mean(axis=1)
    sorted_idx = np.argsort(avg_similarities)

    print("\nArchivos más distintos al promedio (necesitan atención):")
    for i in sorted_idx[:5]:
        print(f"  {results[i]['file']}: SO={avg_similarities[i]:.3f}")

    print("\nArchivos más similares al promedio (bien estructurados):")
    for i in sorted_idx[-5:]:
        print(f"  {results[i]['file']}: SO={avg_similarities[i]:.3f}")


if __name__ == "__main__":
    main()
