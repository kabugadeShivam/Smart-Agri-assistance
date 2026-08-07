from pathlib import Path
import faiss
import pickle
from sentence_transformers import SentenceTransformer

ROOT = Path(__file__).resolve().parent.parent

VECTOR_DIR = ROOT / "vector_db"

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index(str(VECTOR_DIR / "agri_index.faiss"))

with open(VECTOR_DIR / "metadata.pkl", "rb") as f:
    metadata = pickle.load(f)


def search(query, k=3):

    embedding = model.encode(
        [query],
        convert_to_numpy=True
    )

    distances, indices = index.search(
        embedding,
        k
    )

    results = []

    for idx in indices[0]:

        if idx < len(metadata):
            results.append(metadata[idx])

    return results