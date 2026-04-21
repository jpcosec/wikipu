"""
FACE FFT Experiments - Correlation Analysis

Ejecuta experimentos de análisis FFT para detectar patrones en código vs wiki.
Guarda resultados en experiments/.
"""

import sys

sys.path.insert(0, ".")

import json
from pathlib import Path
import numpy as np
import pandas as pd
from datetime import datetime
from src.wiki_compiler.face import FaceAnalyzer, TextToSequence


OUTPUT_DIR = Path("experiments/face")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def get_text(path):
    try:
        return open(path).read()
    except:
        return None


def get_all_files():
    py_files = [f for f in Path("src").rglob("*.py") if "__pycache__" not in str(f)]
    md_files = list(Path("wiki").rglob("*.md"))
    test_files = [f for f in Path("tests").rglob("*.py") if "__pycache__" not in str(f)]
    return {"code": py_files, "wiki": md_files, "tests": test_files}


def run_experiment(name, files, analyzer, min_length=200):
    spectra = {}
    for f in files:
        t = get_text(f)
        if t and len(t) > min_length:
            spectra[f.name] = analyzer.analyze_text(t)
    return spectra


def compare_groups(g1, g2, label):
    if not g1 or not g2:
        return {
            "label": label,
            "so_mean": 0,
            "so_std": 0,
            "corr_mean": 0,
            "corr_std": 0,
        }
    sos, corrs = [], []
    for s1 in list(g1.values())[:10]:
        for s2 in list(g2.values())[:10]:
            m = analyzer.compare_spectra(s1, s2)
            sos.append(m.so)
            corrs.append(m.corr)
    return {
        "label": label,
        "so_mean": np.mean(sos),
        "so_std": np.std(sos),
        "corr_mean": np.mean(corrs),
        "corr_std": np.std(corrs),
        "n_g1": len(g1),
        "n_g2": len(g2),
    }


def compute_group_stats(spectra, analyzer):
    keys = list(spectra.keys())
    if len(keys) < 2:
        return {"within_so": 0, "within_corr": 0, "count": len(keys)}

    sos, corrs = [], []
    for i in range(min(15, len(keys))):
        for j in range(i + 1, min(15, len(keys))):
            m = analyzer.compare_spectra(spectra[keys[i]], spectra[keys[j]])
            sos.append(m.so)
            corrs.append(m.corr)

    return {
        "within_so": np.mean(sos) if sos else 0,
        "within_corr": np.mean(corrs) if corrs else 0,
        "count": len(keys),
    }


# ===== EXPERIMENTO PRINCIPAL =====
print("=== FACE FFT Experiments ===\n")

results = {
    "timestamp": datetime.now().isoformat(),
    "experiments": [],
}

# Analizador con z-score (mejores resultados)
analyzer = FaceAnalyzer(preprocess="zscore")

# Obtener archivos
files = get_all_files()
print(
    f"Archivos: code={len(files['code'])}, wiki={len(files['wiki'])}, tests={len(files['tests'])}"
)

# Experimento 1: Código vs Wiki vs Tests
print("\n--- Exp 1: Grupos principales ---")
code_spectra = run_experiment("code", files["code"], analyzer)
wiki_spectra = run_experiment("wiki", files["wiki"], analyzer)
test_spectra = run_experiment("tests", files["tests"], analyzer)

exp1_results = {
    "name": "grupos_principales",
    "code_stats": compute_group_stats(code_spectra, analyzer),
    "wiki_stats": compute_group_stats(wiki_spectra, analyzer),
    "test_stats": compute_group_stats(test_spectra, analyzer),
    "code_vs_wiki": compare_groups(code_spectra, wiki_spectra, "code_vs_wiki"),
    "code_vs_tests": compare_groups(code_spectra, test_spectra, "code_vs_tests"),
    "wiki_vs_tests": compare_groups(wiki_spectra, test_spectra, "wiki_vs_tests"),
}
results["experiments"].append(exp1_results)

print(
    f"  Code: SO={exp1_results['code_stats']['within_so']:.3f}, CORR={exp1_results['code_stats']['within_corr']:.3f}"
)
print(
    f"  Wiki: SO={exp1_results['wiki_stats']['within_so']:.3f}, CORR={exp1_results['wiki_stats']['within_corr']:.3f}"
)
print(
    f"  Tests: SO={exp1_results['test_stats']['within_so']:.3f}, CORR={exp1_results['test_stats']['within_corr']:.3f}"
)
print(f"  Code vs Wiki: SO={exp1_results['code_vs_wiki']['so_mean']:.3f}")

# Experimento 2: Archivos por tamaño (chico/mediano/grande)
print("\n--- Exp 2: Tamaño de archivos ---")
small = {k: v for k, v in code_spectra.items() if len(list(v[0])) < 300}
medium = {k: v for k, v in code_spectra.items() if 300 <= len(list(v[0])) < 600}
large = {k: v for k, v in code_spectra.items() if len(list(v[0])) >= 600}

exp2_results = {
    "name": "tamano_archivos",
    "small": compute_group_stats(small, analyzer),
    "medium": compute_group_stats(medium, analyzer),
    "large": compute_group_stats(large, analyzer),
}
results["experiments"].append(exp2_results)

print(
    f"  Small: {small.get('count', len(small))} files, SO={exp2_results['small']['within_so']:.3f}"
)
print(f"  Medium: {len(medium)} files, SO={exp2_results['medium']['within_so']:.3f}")
print(f"  Large: {len(large)} files, SO={exp2_results['large']['within_so']:.3f}")

# Experimento 3: Con diferentes encoders
print("\n--- Exp 3: Encoders ---")
encoders = {
    "char_codes": TextToSequence.char_codes,
    "word_lengths": TextToSequence.word_lengths,
    "sentence_lengths": TextToSequence.sentence_lengths,
}

exp3_results = {"name": "encoders", "results": {}}
for enc_name, enc_func in encoders.items():
    analyzer_enc = FaceAnalyzer(preprocess="zscore")
    analyzer_enc.set_encoder(type("E", (), {"char_codes": staticmethod(enc_func)})())

    enc_code = run_experiment(
        f"enc_{enc_name}", files["code"], analyzer_enc, min_length=100
    )
    enc_wiki = run_experiment(
        f"enc_{enc_name}", files["wiki"], analyzer_enc, min_length=100
    )

    comparison = compare_groups(enc_code, enc_wiki, enc_name)
    exp3_results["results"][enc_name] = {
        "code_count": len(enc_code),
        "wiki_count": len(enc_wiki),
        "code_vs_wiki_so": comparison["so_mean"],
        "code_vs_wiki_corr": comparison["corr_mean"],
    }

results["experiments"].append(exp3_results)
print(
    f"  char_codes: SO={exp3_results['results']['char_codes']['code_vs_wiki_so']:.3f}"
)
print(
    f"  word_lengths: SO={exp3_results['results']['word_lengths']['code_vs_wiki_so']:.3f}"
)

# Experimento 4: Con diferentes preprocesos
print("\n--- Exp 4: Preprocesamiento ---")
preprocs = ["none", "zscore", "log", "minmax"]
exp4_results = {"name": "preprocessing", "results": {}}

for p in preprocs:
    analyzer_p = FaceAnalyzer(preprocess=p)
    p_code = run_experiment(f"pre_{p}", files["code"], analyzer_p)
    p_wiki = run_experiment(f"pre_{p}", files["wiki"], analyzer_p)
    comp = compare_groups(p_code, p_wiki, p)
    exp4_results["results"][p] = {
        "code_vs_wiki_so": comp["so_mean"],
        "code_vs_wiki_corr": comp["corr_mean"],
    }

results["experiments"].append(exp4_results)
print(f"  none: SO={exp4_results['results']['none']['code_vs_wiki_so']:.3f}")
print(f"  zscore: SO={exp4_results['results']['zscore']['code_vs_wiki_so']:.3f}")

# Experimento 5: Comparación de archivos individuales con promedio
print("\n--- Exp 5: Distancia al promedio ---")

avg_code = (
    analyzer.average_spectrum(list(code_spectra.values()))
    if code_spectra
    else (np.array([]), np.array([]))
)
avg_wiki = (
    analyzer.average_spectrum(list(wiki_spectra.values()))
    if wiki_spectra
    else (np.array([]), np.array([]))
)

distances = {"code": [], "wiki": []}
for name, spec in code_spectra.items():
    m = analyzer.compare_spectra(spec, avg_code)
    distances["code"].append({"name": name, "so": m.so, "corr": m.corr})

for name, spec in wiki_spectra.items():
    m = analyzer.compare_spectra(spec, avg_wiki)
    distances["wiki"].append({"name": name, "so": m.so, "corr": m.corr})

exp5_results = {
    "name": "distancia_promedio",
    "code_avg_so": np.mean([d["so"] for d in distances["code"]])
    if distances["code"]
    else 0,
    "code_avg_corr": np.mean([d["corr"] for d in distances["code"]])
    if distances["code"]
    else 0,
    "wiki_avg_so": np.mean([d["so"] for d in distances["wiki"]])
    if distances["wiki"]
    else 0,
    "wiki_avg_corr": np.mean([d["corr"] for d in distances["wiki"]])
    if distances["wiki"]
    else 0,
}
results["experiments"].append(exp5_results)

print(f"  Code avg SO: {exp5_results['code_avg_so']:.3f}")
print(f"  Wiki avg SO: {exp5_results['wiki_avg_so']:.3f}")

# ===== GUARDAR RESULTADOS =====
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = OUTPUT_DIR / f"experiments_{timestamp}.json"
with open(output_file, "w") as f:
    json.dump(results, f, indent=2, default=str)

print(f"\n=== Resultados guardados en {output_file} ===")
