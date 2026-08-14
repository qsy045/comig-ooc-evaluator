from sentence_transformers import SentenceTransformer, util

print("正在加载语义模型，请稍候...")
# 1. 加载轻量级多语言模型（第一次运行会自动下载模型权重，约 400MB）
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

# 2. 准备两句对话（模拟官方台词与 AI/玩家回复）
official_script = "即使全世界都站在你的对立面，我也永远会在你身后。"
ai_reply = "别担心，无论遇到什么困难，我都不会离开你。"

# 3. 计算语义向量与相似度得分
emb1 = model.encode(official_script)
emb2 = model.encode(ai_reply)
similarity = util.cos_sim(emb1, emb2).item()

# 4. 打印最终结果
print("\n" + "="*45)
print("🎉 恭喜！你的 Mac 成功跑通了第一个 Python Embedding 项目！")
print(f"官方台词: {official_script}")
print(f"AI/玩家回复: {ai_reply}")
print(f"语义相似度得分 (0-1区间): {similarity:.4f}")
print("="*45 + "\n")