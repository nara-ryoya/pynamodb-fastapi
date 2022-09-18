from pynamodb.attributes import (
    BinaryAttribute,
    MapAttribute,
    NumberAttribute,
    UnicodeAttribute,
    UTCDateTimeAttribute,
)
from pynamodb.indexes import AllProjection, GlobalSecondaryIndex
from pynamodb.models import Model

from .. import schemas


class BookAttribute(MapAttribute):
    author = UnicodeAttribute()
    category = UnicodeAttribute()
    thoughts = UnicodeAttribute()
    link = UnicodeAttribute()
    price = NumberAttribute()

    @property
    def schema(self) -> schemas.Book:
        return schemas.Book(
            author=self.author,
            category=self.category,
            thoughts=self.thoughts,
            link=self.link,
            price=self.price,
        )


class DoneIndex(GlobalSecondaryIndex):
    class Meta:
        index_name = "list_by_done"
        read_capacity_units = 2
        write_capacity_units = 1
        projection = AllProjection()

    done = UnicodeAttribute(hash_key=True)


class Tsundoku(Model):
    class Meta:
        host: str
        table_name: str
        region: str

    user_id = UnicodeAttribute(hash_key=True)
    timestamp = UTCDateTimeAttribute(range_key=True)
    done = BinaryAttribute()
    done_index = DoneIndex()
    book = BookAttribute()

    @property
    def schema(self) -> schemas.Tsundoku:
        return schemas.Tsundoku(
            user_id=self.user_id,
            timestamp=self.timestamp,
            done=self.done,
            book=self.book.schema,
        )
