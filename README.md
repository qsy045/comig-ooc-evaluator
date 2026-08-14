LLM Out-of-Character (OOC) Evaluator

A Python prototype designed to evaluate semantic consistency and detect Out-of-Character (OOC) boundary breaches in companion and RPG LLM agents. Built as an open-source Proof of Concept (PoC) for socio-emotional AI competence assessment under the **Competence Imitation Game (COMIG)** framework.

> **Project Status & Methodology Note:**  
> This prototype was developed by the author, with implementation assisted by Generative AI code tooling for rapid prototyping and validation.


## 🌟 Key Features

- **Semantic Vector Embedding**: Employs `paraphrase-multilingual-MiniLM-L12-v2` via `sentence-transformers` to quantify cosine semantic similarity between baseline narrative benchmarks and candidate responses.
- **Automated Consistency Scoring**: Computes objective semantic alignment scores to systematically capture deviations from target persona constraints.
- **Multilingual Support**: Supports both English and multilingual text inputs (e.g., game scripts, localized player interactions, and fan community benchmarks).

1. Installation
Install the lightweight sentence embedding library:
```bash
pip install sentence-transformers

2. Execution
Run the evaluation script directly:

Bash
python evaluator_poc.py
📊 Sample Output
Plaintext
Loading semantic embedding model...

==================================================
Semantic Consistency Evaluation Output
==================================================
Official Baseline: 即使全世界都站在你的对立面，我也永远会在你身后。
Candidate Reply:   别担心，无论遇到什么困难，我都不会离开你。
Cosine Similarity (0-1 range): 0.8524
==================================================

