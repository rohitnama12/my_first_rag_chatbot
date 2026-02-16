# ⚡ Fast RAG Chatbot (Groq + Pinecone + Sentence-Transformers)

Ek simple aur efficient **RAG (Retrieval-Augmented Generation)** chatbot jo Groq Cloud API ka use karke fast answers deta hai. Is project mein humne local embeddings use kiye hain taaki cost zero rahe aur performance top-notch ho.



## 🚀 Features

* **Ultra Fast:** Groq Llama-3 API ka use karke lightning-fast responses.
* **Cost Effective:** Sentence-Transformers (Local) use kiye hain embeddings ke liye, koi Google/OpenAI API cost nahi.
* **Dynamic Indexing:** PDF upload karte hi Pinecone mein naya index ban jata hai.
* **Clean Structure:** Professional folder structure (Core, Services, Models) ka use kiya gaya hai.

## 🛠️ Tech Stack

* **LLM:** Groq (Llama 3.1 8B)
* **Vector Database:** Pinecone
* **Embeddings:** HuggingFace (all-MiniLM-L6-v2)
* **Frontend:** Gradio
* **Language:** Python 3.12

## 📁 Project Structure

```text
app/
├── api/       # Gradio UI logic
├── core/      # API Keys aur configuration
├── models/    # Data schemas aur dataclasses
└── services/  # PDF processing, Vector store aur LLM logic
main.py        # Project entry point
