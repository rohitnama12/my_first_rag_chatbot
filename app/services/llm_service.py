from groq import Groq
from app.core.config import settings

client = Groq(api_key=settings.GROQ_API_KEY)

def generate_rag_response(query, context):
    prompt = f"""
    You are a helpful assistant. Use the context below to answer the question.
    If the context doesn't contain the answer, say so.
    
    Context:
    {context}
    
    Question: 
    {query}
    """
    
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.1-8b-instant", # Using Llama 3 on Groq (Fast!)
    )

    return chat_completion.choices[0].message.content