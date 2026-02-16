import os
from dotenv import load_dotenv

dotenv_path = "/Users/rohitnama/Desktop/LANGCHAIN/.env"
load_dotenv(dotenv_path)

class Config:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2" 
    PINECONE_INDEX_NAME = "groq-rag-chatbot" 

settings = Config()