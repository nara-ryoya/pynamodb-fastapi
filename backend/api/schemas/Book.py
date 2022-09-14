from typing import Optional
from pydantic import BaseModel, Field

class BookAttribute(BaseModel):
    author: str
    category: Optional[str]
    thoughts: Optional[str] = Field(description="感想")
    link: Optional[str]
    price: Optional[int]