from typing import List

from fastapi import APIRouter

from ..schemas import OK, User

users_router = APIRouter()


@users_router.get("/user/overall", response_model=List[User])
def list_overall_user() -> List[User]:
    return []


@users_router.post("/user", response_model=OK)
def add_user(user: User) -> OK:
    return OK
