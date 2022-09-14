from typing import List

from fastapi import APIRouter

from ..schemas import OK, Tsundoku

tsundoku_router = APIRouter()


@tsundoku_router.get("/tsundoku/{user_id}", response_model=List[Tsundoku])
def list_books_by_user_id(user_id: str) -> List[Tsundoku]:
    return []


@tsundoku_router.post("/tsundoku", response_model=List[Tsundoku])
def add_tsundoku(tsundoku: Tsundoku) -> OK:
    return OK
