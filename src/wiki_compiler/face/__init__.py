import argparse
from pathlib import Path
from typing import Union, List, Optional
import numpy as np
import pandas as pd
from scipy import interpolate
from scipy.stats import pearsonr, spearmanr
from scipy.fft import fft, fftfreq, fftshift
from dataclasses import dataclass


@dataclass
class FaceMetrics:
    so: float
    corr: float
    sam: float
    spear: float


class FFTProcessor:
    def __init__(self, preprocess: str = "none"):
        self.preprocess = preprocess

    def _preprocess_data(self, data: np.ndarray) -> np.ndarray:
        if self.preprocess == "zscore":
            return (data - np.mean(data)) / (np.std(data) + 1e-6)
        elif self.preprocess == "log":
            return np.log(np.abs(data) + 1)
        elif self.preprocess == "logzs":
            log_data = np.log(np.abs(data) + 1)
            return (log_data - np.mean(log_data)) / (np.std(log_data) + 1e-6)
        elif self.preprocess == "minmax":
            min_val, max_val = np.min(data), np.max(data)
            return (data - min_val) / (max_val - min_val + 1e-10)
        return data

    def compute_fft(self, sequence: np.ndarray) -> tuple:
        data = self._preprocess_data(sequence)
        N = len(data)
        if N < 2:
            return np.array([]), np.array([])

        freq = fftshift(fftfreq(N))
        fft_res = fftshift(fft(data))
        power = np.abs(fft_res)
        return freq[N // 2 :], power[N // 2 :]

    def compute_fft_batch(self, sequences: List[np.ndarray]) -> List[tuple]:
        results = []
        for seq in sequences:
            if len(seq) > 1:
                results.append(self.compute_fft(seq))
            else:
                results.append((np.array([]), np.array([])))
        return results


class SpectrumComparator:
    def __init__(self, resolution: int = 1000):
        self.resolution = resolution

    def align_spectra(
        self,
        freqs1: np.ndarray,
        powers1: np.ndarray,
        freqs2: np.ndarray,
        powers2: np.ndarray,
    ) -> tuple:
        if len(freqs1) < 2 or len(freqs2) < 2:
            return np.array([]), np.array([]), np.array([])

        x = np.linspace(0, 0.5, self.resolution)
        f1 = interpolate.interp1d(
            freqs1, powers1, fill_value="extrapolate", assume_sorted=True
        )
        f2 = interpolate.interp1d(
            freqs2, powers2, fill_value="extrapolate", assume_sorted=True
        )
        return x, f1(x), f2(x)

    def spectral_overlap(self, y1: np.ndarray, y2: np.ndarray) -> float:
        y1, y2 = np.abs(y1), np.abs(y2)
        intersection = np.minimum(y1, y2)
        roof = np.maximum(y1, y2)
        area_int = np.trapz(intersection, dx=1 / len(y1))
        area_roof = np.trapz(roof, dx=1 / len(y1))
        return area_int / (area_roof + 1e-10)

    def spectral_angle_mapper(self, y1: np.ndarray, y2: np.ndarray) -> float:
        y1_norm = y1 / (np.linalg.norm(y1) + 1e-10)
        y2_norm = y2 / (np.linalg.norm(y2) + 1e-10)
        dot = np.dot(y1_norm, y2_norm)
        return np.arccos(np.clip(dot, -1, 1)) / np.pi

    def pearson_correlation(self, y1: np.ndarray, y2: np.ndarray) -> float:
        try:
            return pearsonr(y1, y2)[0]
        except:
            return 0.0

    def spearman_correlation(self, y1: np.ndarray, y2: np.ndarray) -> float:
        try:
            return spearmanr(y1, y2)[0]
        except:
            return 0.0

    def compare(
        self,
        freq1: np.ndarray,
        power1: np.ndarray,
        freq2: np.ndarray,
        power2: np.ndarray,
    ) -> FaceMetrics:
        x, y1, y2 = self.align_spectra(freq1, power1, freq2, power2)
        if len(x) < 2:
            return FaceMetrics(so=0.0, corr=0.0, sam=0.0, spear=0.0)
        return FaceMetrics(
            so=self.spectral_overlap(y1, y2),
            corr=self.pearson_correlation(y1, y2),
            sam=self.spectral_angle_mapper(y1, y2),
            spear=self.spearman_correlation(y1, y2),
        )


class TextToSequence:
    @staticmethod
    def char_codes(text: str) -> np.ndarray:
        return np.array([ord(c) for c in text], dtype=np.float64)

    @staticmethod
    def token_length(text: str) -> np.ndarray:
        words = text.split()
        return np.array([len(w) for w in words], dtype=np.float64)

    @staticmethod
    def word_lengths(text: str) -> np.ndarray:
        return np.array([len(w) for w in text.split()], dtype=np.float64)

    @staticmethod
    def sentence_lengths(text: str) -> np.ndarray:
        sentences = text.replace("!", ".").replace("?", ".").split(".")
        return np.array(
            [len(s.split()) for s in sentences if s.strip()], dtype=np.float64
        )

    @staticmethod
    def punctuation_density(text: str, window: int = 10) -> np.ndarray:
        punct = set(".,!?;:\"'")
        result = []
        for i in range(len(text)):
            start = max(0, i - window)
            count = sum(1 for c in text[start : i + 1] if c in punct)
            result.append(count / (i - start + 1))
        return np.array(result, dtype=np.float64)

    @staticmethod
    def char_ngrams(text: str, n: int = 2) -> np.ndarray:
        ngrams = [hash(text[i : i + n]) % 1000 for i in range(len(text) - n + 1)]
        return np.array(ngrams, dtype=np.float64)


class FaceAnalyzer:
    def __init__(self, preprocess: str = "none", resolution: int = 1000):
        self.fft = FFTProcessor(preprocess)
        self.comparator = SpectrumComparator(resolution)
        self.sequence_encoder = TextToSequence()

    def set_encoder(self, encoder):
        self.sequence_encoder = encoder

    def encode_text(self, text: str) -> np.ndarray:
        return self.sequence_encoder.char_codes(text)

    def analyze_text(self, text: str) -> tuple:
        sequence = self.encode_text(text)
        return self.fft.compute_fft(sequence)

    def analyze_texts(self, texts: List[str]) -> List[tuple]:
        sequences = [self.encode_text(t) for t in texts]
        return self.fft.compute_fft_batch(sequences)

    def compare_texts(self, text1: str, text2: str) -> FaceMetrics:
        freq1, power1 = self.analyze_text(text1)
        freq2, power2 = self.analyze_text(text2)
        return self.comparator.compare(freq1, power1, freq2, power2)

    def compare_spectra(self, spectrum1: tuple, spectrum2: tuple) -> FaceMetrics:
        return self.comparator.compare(
            spectrum1[0], spectrum1[1], spectrum2[0], spectrum2[1]
        )

    def average_spectrum(self, spectra: List[tuple]) -> tuple:
        valid = [(s[0], s[1]) for s in spectra if len(s[0]) > 1]
        if not valid:
            return np.array([]), np.array([])

        min_len = min(len(f) for f, _ in valid)
        freqs = valid[0][0][:min_len]
        powers = np.mean([p[:min_len] for _, p in valid], axis=0)
        return freqs, powers

    def cluster_spectra(self, spectra: List[tuple], method: str = "avg") -> dict:
        if not spectra:
            return {}

        valid = [s for s in spectra if len(s[0]) > 1]
        if not valid:
            return {"avg": (np.array([]), np.array([]))}

        avg = self.average_spectra(valid)
        return {"average": avg}


def load_texts_from_file(path: str) -> List[str]:
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def load_texts_from_files(paths: List[str]) -> List[str]:
    texts = []
    for path in paths:
        texts.extend(load_texts_from_file(path))
    return texts


def save_spectrum(freq: np.ndarray, power: np.ndarray, output_path: str):
    df = pd.DataFrame({"freq": freq, "power": power})
    df.to_csv(output_path, index=False)


def save_spectrum_group(spectra: List[tuple], output_dir: str):
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    for i, (freq, power) in enumerate(spectra):
        save_spectrum(freq, power, f"{output_dir}/spectrum_{i:04d}.csv")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="FACE FFT Analyzer")
    parser.add_argument("--input", "-i", type=str, help="Input text file(s)", nargs="+")
    parser.add_argument("--output", "-o", type=str, help="Output FFT CSV")
    parser.add_argument(
        "--preprocess",
        "-p",
        type=str,
        default="none",
        choices=["none", "zscore", "log", "logzs", "minmax"],
    )
    parser.add_argument(
        "--encoder",
        "-e",
        type=str,
        default="char_codes",
        choices=["char_codes", "word_lengths", "sentence_lengths", "char_ngrams"],
    )
    args = parser.parse_args()

    encoders = {
        "char_codes": TextToSequence.char_codes,
        "word_lengths": TextToSequence.word_lengths,
        "sentence_lengths": TextToSequence.sentence_lengths,
        "char_ngrams": lambda t: TextToSequence.char_ngrams(t, 2),
    }

    analyzer = FaceAnalyzer(preprocess=args.preprocess)
    analyzer.set_encoder(type("Encoder", (), {"char_codes": encoders[args.encoder]})())

    if args.input:
        texts = load_texts_from_files(args.input)
        spectra = analyzer.analyze_texts(texts)

        if args.output:
            all_freq = np.concatenate([s[0] for s in spectra if len(s[0]) > 0])
            all_power = np.concatenate([s[1] for s in spectra if len(s[1]) > 0])
            save_spectrum(all_freq, all_power, args.output)
        else:
            print(f"Analyzed {len(texts)} texts")
