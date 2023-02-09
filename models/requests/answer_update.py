from typing import List, Optional
from pydantic import BaseModel

class AnswerUpdate(BaseModel):
    categoria: Optional[str] = None
    response: Optional[str] = None