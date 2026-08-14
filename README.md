# LLM Out-of-Character (OOC) Evaluator

A lightweight Python prototype designed to evaluate semantic consistency and detect Out-of-Character (OOC) boundary breaches in companion/RPG LLM agents. Built as a proof-of-concept for socio-emotional AI competence assessment under the COMIG framework.

## Key Features
- **Semantic Vector Embedding**: Uses `paraphrase-multilingual-MiniLM-L12-v2` via `sentence-transformers` to quantify semantic similarity between LLM candidate outputs, character personas, and human expert baselines.
- **Automated OOC Alerting**: Calculates a weighted combined score to automatically flag high-risk OOC responses (e.g., generic AI clichés, tone mismatch).
- **Language-Agnostic Architecture**: Supports both English and multilingual text inputs (e.g., game dialogues, fanfiction baselines).

##  Quick Start

###  Installation
```bash
pip install sentence-transformers
