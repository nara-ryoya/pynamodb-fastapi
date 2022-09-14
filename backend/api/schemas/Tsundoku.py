from datetime import datetime
from pydantic import BaseModel


class Tsundoku(BaseModel):
    user_id: str
    timestamp: datetime
    done: bool