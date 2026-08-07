from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Model Loaded Successfully!")

embedding = model.encode("Tomato Late Blight")

print("Embedding Length:", len(embedding))