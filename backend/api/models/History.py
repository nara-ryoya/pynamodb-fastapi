from pynamodb.attributes import (
    MapAttribute,
    NumberAttribute,
    UnicodeAttribute,
    UTCDateTimeAttribute,
)
from pynamodb.indexes import AllProjection, GlobalSecondaryIndex
from pynamodb.models import Model

from .. import schemas
from ..settings import get_settings


class BookAttribute(MapAttribute):
    author = UnicodeAttribute()
    category = UnicodeAttribute()
    title = UnicodeAttribute()
    thoughts = UnicodeAttribute()
    link = UnicodeAttribute(null=True)
    price = NumberAttribute()

    @property
    def schema(self) -> schemas.Book:
        return schemas.Book(
            author=self.author,
            category=self.category,
            thoughts=self.thoughts,
            title=self.title,
            link=self.link,
            price=self.price,
        )


class UserIDIndex(GlobalSecondaryIndex):
    class Meta:
        index_name = "list_by_user_id"
        read_capacity_units = 2
        write_capacity_units = 1
        projection = AllProjection()

    user_id = UnicodeAttribute(hash_key=True)


class History(Model):
    DEFAULT_HASH = "default"

    class Meta:
        host: str
        table_name: str
        region: str

    @classmethod
    def set_meta(cls) -> None:
        settings = get_settings()
        cls.Meta.host = settings.table_host
        cls.Meta.table_name = settings.table_name
        cls.Meta.region = settings.region

    hash = UnicodeAttribute(hash_key=True, default=DEFAULT_HASH)
    timestamp = UTCDateTimeAttribute(range_key=True)
    user_id_index = UserIDIndex()
    user_id = UnicodeAttribute()
    book = BookAttribute()

    @property
    def schema(self) -> schemas.History:
        return schemas.History(
            user_id=self.user_id,
            timestamp=self.timestamp,
            book=self.book.schema,
        )
