from typing import List

from fastapi import APIRouter

from ..schemas import OK, History

history_router = APIRouter()


@history_router.get("/history/{user_id}", response_model=List[History])
def list_books_by_user_id(user_id: str) -> List[History]:
    return []


@history_router.post("/history", response_model=str)
def add_tsundoku(tsundoku: History) -> str:
    return OK
