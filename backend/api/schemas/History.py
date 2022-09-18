from datetime import datetime

from pydantic import BaseModel

from .Book import Book


class History(BaseModel):
    user_id: str
    timestamp: datetime
    book: Book
