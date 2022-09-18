from datetime import datetime
from typing import List

from fastapi import APIRouter

from ..schemas import OK, History, Book
from .. import crud

history_router = APIRouter()


@history_router.get("/history/{user_id}", response_model=List[History])
def list_by_user_id(user_id: str) -> List[History]:
    return [record.schema for record in crud.history.list_by_user_id(user_id=user_id)]


@history_router.get("/history", response_model=List[History])
def list_by_date(start: datetime, end: datetime) -> List[History]:
    return [
        record.schema
        for record in crud.history.list_by_datetime(start_date=start, end_date=end)
    ]


@history_router.post("/history", response_model=str)
def add_tsundoku(user_id, book: Book) -> str:
    crud.history.add_history(user_id=user_id, book=book)
    return OK
