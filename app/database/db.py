import os

from tinydb import TinyDB, Query
from tinydb.table import Document

from database.forms import forms 

db_name = "db.json"

cwd = os.getcwd()
db_path = os.path.join(cwd, "database", db_name)
database_exists = os.path.exists(db_path)

db = TinyDB(db_path)

forms_table = db.table("forms")
fields_table = db.table("fields")

if not database_exists:
    for form in forms:
        forms_table.insert(form)


def find_forms_by_fields(*args) -> list[Document]:
    q = forms_table.search(
        Query().form_fields.test(lambda x: set(x).issubset(set(args)))
    )
    return q

