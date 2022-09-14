from pynamodb.attributes import MapAttribute, UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.indexes import AllProjection, GlobalSecondaryIndex
from pynamodb.models import Model


class Book(MapAttribute):
    author = UnicodeAttribute()
    category = UnicodeAttribute()
    thoughts = UnicodeAttribute()


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
    done = UnicodeAttribute()
    done_index = DoneIndex()
