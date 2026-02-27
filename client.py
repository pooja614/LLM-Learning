from chromadb import Client
from chromadb.config import Settings
# from langchain.embeddings import OpenAIEmbeddings 
from langchain_chroma import Chroma
from sentence_transformers import SentenceTransformer

# ---------- Embedding Model ----------------------
def get_embedding_model():
    model = SentenceTransformer("all-MiniLM-L6-v2")
    return model

def get_vector_store(collection_name: str = "schema_metadata"):
    embeddings = get_embedding_model()

    vectordb = Chroma(
        collection_name = collection_name, 
        
    )