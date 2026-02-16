from dataclasses import dataclass
from typing import List, Optional

# 1. Document Chunk ka structure
@dataclass
class DocumentChunk:
    text: str
    chunk_id: str
    score: Optional[float] = None
    source: str = "uploaded_pdf"

# 2. Chat Response ka structure
@dataclass
class ChatResponse:
    answer: str
    context_used: List[DocumentChunk]
    model_name: str = "llama-3.1-8b-instant"