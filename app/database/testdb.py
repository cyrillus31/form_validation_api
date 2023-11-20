import os

from tinydb import TinyDB, Query

db_name = "testdb.json"

cwd = os.getcwd()
database_exists = os.path.exists(os.path.join(cwd, "database", db_name))
if database_exists:
    os.remove(os.path.join(cwd, "database", db_name))

db = TinyDB(os.path.join(cwd, "database", "testdb.json"))
forms_table = db.table("forms")
fields_table = db.table("fields")

forms = [
    {
        "form_name": "Client",
        "form_fields": ["name", "date registered", "email", "phone number"],
    },
    {"form_name": "Order", "form_fields": ["description", "date created", "email"]},
    {"form_name": "Seller", "form_fields": ["name", "phone"]}
]


fields_types = {
    "name": "text",
    "date registered": "date",
    "email": "email",
    "phone number": "phone",
    "description": "text",
    "date created": "date",
    "phone": "phone"
}


# for field in fields_types:
#     fields_table.insert({"field name": field, "field type": fields_types[field]})

for form in forms:
    forms_table.insert(form)

def find_forms_by_fields(*args):
    q = forms_table.search(Query().form_fields.test(lambda x: set(args).issubset(set(x))))
    return q


