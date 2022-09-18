from datetime import datetime
from typing import List

from dateutil.relativedelta import relativedelta
from fastapi import APIRouter

from .. import crud
from ..schemas import OK, Book, History

history_router = APIRouter()


@history_router.get("/history/{user_id}", response_model=List[History])
def list_by_user_id(user_id: str) -> List[History]:
    return [record.schema for record in crud.history.list_by_user_id(user_id=user_id)]


@history_router.get("/history", response_model=List[History])
def list_by_date(year: int, month: int) -> List[History]:
    return [
        record.schema
        for record in crud.history.list_by_datetime(
            start_date=datetime(year=year, month=month, day=1),
            end_date=datetime(year=year, month=month, day=1)
            + relativedelta(months=1)
            - relativedelta(days=1),
        )
    ]


@history_router.post("/history", response_model=str)
def add_tsundoku(user_id, book: Book) -> str:
    crud.history.add_history(user_id=user_id, book=book)
    return OK
