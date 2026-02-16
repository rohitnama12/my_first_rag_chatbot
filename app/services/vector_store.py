import time
import hashlib
from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer
from app.core.config import settings

# Initialize components once
pc = Pinecone(api_key=settings.PINECONE_API_KEY)
embedder = SentenceTransformer(settings.EMBEDDING_MODEL_NAME)

def generate_id(text):
    return hashlib.sha256(text.encode()).hexdigest()

def get_embedding(text):
    # Returns a list of floats (vector)
    return embedder.encode(text).tolist()

def setup_index(index_name):
    existing_indexes = [index.name for index in pc.list_indexes()]
    
    # Check if index exists, if not create it
    if index_name not in existing_indexes:
        # Get dimension from the model (384 for MiniLM)
        sample_embedding = get_embedding("test")
        dimension = len(sample_embedding)
        
        pc.create_index(
            name=index_name,
            dimension=dimension,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )
        time.sleep(2) # Wait for initialization

    return pc.Index(index_name)

def upsert_vectors(chunks, index_name):
    index = setup_index(index_name)
    vectors = []
    
    for chunk in chunks:
        vector = get_embedding(chunk)
        chunk_id = generate_id(chunk)
        
        vectors.append({
            "id": chunk_id,
            "values": vector,
            "metadata": {"text": chunk}
        })
    
    # Upsert in batches if needed, but simple for now
    index.upsert(vectors=vectors)
    return index

def query_vectors(query, index, n_results=3):
    query_vector = get_embedding(query)
    
    results = index.query(
        vector=query_vector,
        top_k=n_results,
        include_metadata=True
    )
    
    context_text = "\n\n".join([match['metadata']['text'] for match in results['matches']])
    return context_text