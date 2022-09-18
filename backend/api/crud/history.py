from datetime import datetime

from pynamodb.pagination import ResultIterator

from .. import models, schemas


def list_by_user_id(user_id: str) -> ResultIterator[models.History]:
    return models.History.query(
        models.History.DEFAULT_HASH, models.History.user_id == user_id
    )


def list_by_datetime(
    start_date: datetime, end_date: datetime
) -> ResultIterator[models.History]:
    return models.History.query(
        models.History.DEFAULT_HASH,
        models.History.timestamp.between(start_date, end_date),
    )


def add_history(user_id: str, book: schemas.Book) -> None:
    tsundoku = models.History(
        **schemas.History(user_id=user_id, timestamp=datetime.now(), book=book).dict()
    )
    tsundoku.save()
