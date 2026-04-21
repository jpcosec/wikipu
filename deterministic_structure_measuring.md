# Deterministic Structure Measuring

## Overview

This document describes the framework for measuring deterministic structure in text, code, and documentation using FFT-based spectral analysis and Markov chain entropy.

## Problem Statement

We want to measure:
1. **Code quality**: clean code vs spaghetti code
2. **Text classification**: human-written vs AI-generated
3. **Structural consistency**: how coherent is a codebase
4. **Entropy/Stability**: how predictable is a text

## Architecture

### 1. FFT Spectral Analysis (`src/wiki_compiler/face/`)

**Purpose**: Transform any sequence into frequency domain to detect patterns.

**Pipeline**:
```
Text → Sequence (char codes, word lengths, etc.) → FFT → Spectrum → Compare
```

**Components**:
- `FFTProcessor`: Computes FFT with configurable preprocessing (none, zscore, log, minmax)
- `SpectrumComparator`: Calculates similarity metrics between spectra
- `FaceAnalyzer`: Unified interface for text analysis
- `TextToSequence`: Different encoders (char_codes, word_lengths, sentence_lengths, char_ngrams)

**Metrics**:
- **SO** (Spectral Overlap): Area of intersection / area of union
- **CORR** (Pearson): Linear correlation between spectra
- **SAM** (Spectral Angle Mapper): Angular difference
- **SPEAR** (Spearman): Rank correlation

### 3. Structural Abstraction (`src/structural_abstraction/`)

**Purpose**: Measure structure at code level (functions, classes, patterns) instead of individual tokens.

**Pipeline**:
```
Code → AST Parse → Extract Functions/Classes → Sequence → N-gram Model → Entropy
```

**Components**:
- `StructuralParser`: Uses Python AST to extract function signatures, classes, methods
- `code_to_structural_sequence()`: Converts code to sequence of structural symbols
- `StructuralEntropy`: N-gram model trained on structural sequences

**Structural Symbols**:
- `FUNC_name` - Function name
- `ARG_param` - Parameters
- `CALL_func` - Function calls
- `DEPTH_n` - Nesting depth
- `COMPLEX_n` - Complexity (if/for/while count)
- `CLASS_name`, `INHERIT_X`, `ATTR_y` - Class features

### 2. Markov N-gram Entropy (`src/markov_entropy/`)

**Purpose**: Measure unpredictability using n-gram language models.

**Pipeline**:
```
Text → Tokenize → N-gram Model → NLL sequence → Stats/FFT
```

**Components**:
- `SimpleNGramModel`: N-gram model with Laplace smoothing
- `NGramEntropy`: Compute NLL per token
- `CategoryClassifier`: Classify texts based on entropy

**Metrics**:
- **Entropy**: Mean NLL (higher = more unpredictable)
- **Perplexity**: 2^entropy
- **NLL sequence**: Per-token negative log-likelihood

### 3. Structural Abstraction (Future)

**Purpose**: Measure structure at code level (functions, classes, patterns).

**Idea**: Instead of `calculate(word, probability)`, measure `function(input, input, x)`.

**Implementation** (`src/structural_abstraction/`):
- Uses Python AST to parse functions, classes, methods
- Extracts: function signatures, parameters, return types, complexity, nesting depth, function calls
- Converts to sequence of structural symbols
- Trains N-gram model on structural sequences

**Results** (trained on 30 real code files):

| Code Type | Structural Entropy |
|-----------|-------------------|
| Clean (example) | 10.72 |
| Spaghetti (example) | 9.17 |

Higher entropy = more unpredictable structure pattern

## Experiments & Results

### FFT on Project Code vs Wiki

| Comparison | SO | CORR |
|------------|-----|------|
| Code vs Code (within) | 0.528 | 0.386 |
| Wiki vs Wiki (within) | 0.569 | 0.003 |
| Tests vs Tests (within) | 0.522 | 0.369 |
| Code vs Wiki (cross) | 0.514 | 0.011 |
| Code vs Tests | 0.481 | 0.315 |

**Observation**: Code has higher internal correlation (CORR=0.386) while wiki is less correlated (CORR=0.003). Cross-group comparison shows code and wiki are quite different (SO=0.514).

### By Module (within-group SO)

| Module | SO | Files |
|--------|-----|-------|
| docker | 0.644 | 4 |
| owl_backend | 0.567 | 7 |
| wiki_compiler | 0.542 | 34 |
| commands | 0.544 | 12 |
| utils | 0.398 | 3 |

**Observation**: Some modules are more internally coherent (docker, owl_backend) than others (utils).

### Code Complexity (functions, imports, classes)

| Comparison | SO | CORR |
|------------|-----|------|
| Many imports vs Few imports | 0.094 | -0.999 |
| With classes vs Without classes | 0.023 | 0.568 |
| Simple functions vs Complex | 0.616 | -0.926 |

**Observation**: These structural features create very distinct spectra.

### Preprocessing Methods

| Method | Code vs Wiki SO | Code vs Wiki CORR |
|--------|-----------------|-------------------|
| none | 0.253 | 0.840 |
| zscore | 0.514 | 0.011 |
| log | 0.480 | 0.974 |
| minmax | 0.218 | 0.817 |

**Observation**: zscore gives best separation (low CORR = more distinct).

### Clean vs Spaghetti Code

| Method | SO | CORR |
|--------|-----|------|
| Char codes FFT | 0.664 | 0.658 |
| Word lengths FFT | 0.523 | 0.905 |
| NLL → FFT (Markov) | 0.602 | 0.134 |

### NLL Statistics

| Code Type | Mean NLL | Perplexity |
|-----------|----------|------------|
| Clean | 6.07 | ~434 |
| Spaghetti | 6.42 | ~610 |

## Integration with Energy System

Added to `src/wiki_compiler/energy.py`:

```python
# New fields in SystemicEnergy
fft_code_wiki_so: float       # Spectral overlap between code and wiki
fft_code_wiki_corr: float     # Correlation between code and wiki
fft_code_within_so: float     # Internal code coherence
fft_code_within_corr: float   # Internal code consistency  
fft_complexity_score: float   # Chaos from FFT variance
fft_energy: float             # Energy contribution from FFT metrics
```

New function `calculate_fft_metrics()` computes these automatically.

## Usage Examples

### Basic FFT Analysis
```python
from src.wiki_compiler.face import FaceAnalyzer

analyzer = FaceAnalyzer(preprocess='zscore')
freq, power = analyzer.analyze_text("your code here...")
```

### Compare Two Texts
```python
m = analyzer.compare_texts(text1, text2)
print(f"SO={m.so:.3f}, CORR={m.corr:.3f}")
```

### Markov N-gram Entropy
```python
from src.markov_entropy import NGramEntropy

ne = NGramEntropy(order=2)
ne.train(corpus_texts)
nlls = ne.nll_sequence("test text")
stats = ne.nll_stats("test text")
print(f"Entropy: {stats['entropy']:.2f}")
```

### Category Classification
```python
from src.markov_entropy import CategoryClassifier

ca = CategoryClassifier(order=2)
ca.train_category("clean", clean_texts)
ca.train_category("spaghetti", spaghetti_texts)
result = ca.classify("new code...")
```

### Combined: NLL → FFT
```python
from src.markov_entropy import NGramEntropy
from src.wiki_compiler.face import FaceAnalyzer

# Train model
ne = NGramEntropy(order=2)
ne.train(corpus)

# Get NLL sequence
nlls = ne.nll_sequence(text)

# FFT on NLL
analyzer = FaceAnalyzer(preprocess='zscore')
freq, power = analyzer.fft.compute_fft(nlls)
```

## Future Work: Structural Abstraction

### Concept
Instead of measuring token-level patterns, measure structural patterns:
- Function signatures: `function_name(param1, param2, ...)`
- Class structures: inheritance, methods, attributes
- Control flow patterns: loops, conditionals, nesting depth

### Implementation Ideas

1. **Function Signature Extraction**:
   ```python
   def extract_signatures(code: str) -> list[str]:
       # Parse function definitions
       # Return patterns like "function(a,b,c)"
   ```

2. **Abstraction-Level N-grams**:
   - Bigrams of function calls
   - Patterns like `map(filter(reduce(...)))`
   - Class method chains

3. **AST-Based Analysis**:
   - Use `ast` module to parse Python
   - Extract structural features
   - Measure complexity metrics

### Expected Benefits

- **More robust**: Less sensitive to variable naming
- **Architecture-aware**: Captures design patterns
- **Language-agnostic**: Could work with other parsers
- **Semantic**: Measures "how" not "what"

## Files Created

```
src/wiki_compiler/face/__init__.py     # FFT spectral analysis
src/markov_entropy/__init__.py        # N-gram entropy (tokens)
src/structural_abstraction/__init__.py # Structural entropy (AST)
experiments/face/experiments_*.json   # Results
src/wiki_compiler/energy.py            # Integration
deterministic_structure_measuring.md   # This document
```

## Summary

Three levels of analysis:

1. **Token-level** (FFT on char codes): Quick, language-agnostic, catches basic patterns
2. **Token-level with LM** (Markov N-gram → NLL → FFT): Measures predictability, works for any text
3. **Structure-level** (AST → structural sequence → entropy): Captures code architecture, less dependent on naming

The structural abstraction is the most promising for measuring "code quality" (clean vs spaghetti) because it focuses on how the code is organized rather than what tokens appear.

## References

- FACE: Fourier Analysis of Cross-Entropy (NeurIPS 2023)
- N-gram language models
- Spectral analysis for text classification