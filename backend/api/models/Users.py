from pynamodb.attributes import NumberAttribute, UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.models import Model


class Users(Model):
    class Meta:
        table_name: str
        host: str
        region: str

    user_id = UnicodeAttribute(hash_key=True)
    timestamp = UTCDateTimeAttribute(range_key=True)
    book_counter = NumberAttribute()
    dones_counter = NumberAttribute()
