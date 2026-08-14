"""
Semantic Consistency Evaluator - Proof of Concept (PoC)
Author: Qianyu Sun
Description: A lightweight prototype computing semantic cosine similarity between 
             character dialogue and response candidates using Sentence Transformers.
"""

from sentence_transformers import SentenceTransformer, util

print("Loading semantic embedding model...")
# 1. Load multilingual Sentence-Transformer model
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

# 2. Define test dialogue pairs (e.g., official dialogue baseline vs. candidate reply)
official_script = "即使全世界都站在你的对立面，我也永远会在你身后。"
ai_reply = "别担心，无论遇到什么困难，我都不会离开你。"

# 3. Compute vector embeddings and cosine similarity score
emb1 = model.encode(official_script)
emb2 = model.encode(ai_reply)
similarity = util.cos_sim(emb1, emb2).item()

# 4. Print evaluation output
print("\n" + "=" * 50)
print("Semantic Consistency Evaluation Output")
print("=" * 50)
print(f"Official Baseline: {official_script}")
print(f"Candidate Reply:   {ai_reply}")
print(f"Cosine Similarity (0-1 range): {similarity:.4f}")
print("=" * 50 + "\n")
