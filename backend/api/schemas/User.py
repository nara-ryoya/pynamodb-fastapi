from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    user_id: str
    timestamp: datetime
    book_counter: int
    dones_counter: int
