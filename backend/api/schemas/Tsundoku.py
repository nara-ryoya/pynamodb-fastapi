from datetime import datetime

from pydantic import BaseModel

from .Book import Book


class Tsundoku(BaseModel):
    user_id: str
    timestamp: datetime
    done: bool
    book: Book
