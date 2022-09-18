from api.models import History

History.set_meta()

if History.exists():
    History.delete_table()

History.create_table(read_capacity_units=1, write_capacity_units=1)
