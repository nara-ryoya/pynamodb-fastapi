from api.models import History
from api.settings import get_settings
History.set_meta()

print(History.Meta.host)


if History.exists():
    History.delete_table()

History.create_table(read_capacity_units=1, write_capacity_units=1)
