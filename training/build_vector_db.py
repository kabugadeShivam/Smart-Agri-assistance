from pathlib import Path
import pandas as pd
import faiss
import pickle
from sentence_transformers import SentenceTransformer

# ============================================
# Project Paths
# ============================================

ROOT = Path(__file__).resolve().parent.parent

knowledge_file = ROOT / "agriculture_knowledge.csv"
vector_dir = ROOT / "vector_db"

vector_dir.mkdir(exist_ok=True)

# ============================================
# Load Embedding Model
# ============================================

print("=" * 60)
print("Loading Sentence Transformer...")
print("=" * 60)

model = SentenceTransformer("all-MiniLM-L6-v2")

# ============================================
# Load Knowledge Base
# ============================================

print("\nLoading Agriculture Knowledge Base...\n")

if not knowledge_file.exists():
    print("❌ agriculture_knowledge.csv not found!")
    exit()

df = pd.read_csv(knowledge_file)

print(f"Rows Loaded : {len(df)}")

# Fill missing values
df = df.fillna("")

documents = []
metadata = []

# ============================================
# Create Documents
# ============================================

for _, row in df.iterrows():

    document = f"""
Category: {row.get('Category','')}

Crop: {row.get('Crop','')}

Question:
{row.get('Question','')}

Answer:
{row.get('Answer','')}

Keywords:
{row.get('Keywords','')}
"""

    documents.append(document.strip())

    metadata.append(row.to_dict())

print(f"Documents Created : {len(documents)}")

# ============================================
# Generate Embeddings
# ============================================

print("\nGenerating Embeddings...\n")

embeddings = model.encode(
    documents,
    convert_to_numpy=True,
    show_progress_bar=True,
    batch_size=64
)

print("\nEmbedding Shape :", embeddings.shape)

# ============================================
# Build FAISS Index
# ============================================

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

# ============================================
# Save Files
# ============================================

faiss.write_index(
    index,
    str(vector_dir / "agri_index.faiss")
)

with open(
    vector_dir / "metadata.pkl",
    "wb"
) as f:

    pickle.dump(metadata, f)

print("\n" + "=" * 60)
print("✅ Vector Database Created Successfully!")
print("=" * 60)

print(f"Vectors Stored : {index.ntotal}")
print(f"Embedding Size : {dimension}")

print("\nSaved Files")

print(vector_dir / "agri_index.faiss")
print(vector_dir / "metadata.pkl")