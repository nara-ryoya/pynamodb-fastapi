from pynamodb.attributes import NumberAttribute, UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.models import Model

from .. import schemas


class Users(Model):
    class Meta:
        table_name: str
        host: str
        region: str

    user_id = UnicodeAttribute(hash_key=True)
    timestamp = UTCDateTimeAttribute(range_key=True)
    email = UnicodeAttribute()
    book_counter = NumberAttribute()
    dones_counter = NumberAttribute()

    @property
    def schema(self) -> schemas.User:
        return schemas.User(
            user_id=self.user_id,
            timestamp=self.timestamp,
            email=self.email,
            book_counter=self.book_counter,
            dones_counter=self.dones_counter,
        )
