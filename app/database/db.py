import os

from tinydb import TinyDB, Query

db_name = "db.json"

cwd = os.getcwd()
db_path = os.path.join(cwd, "database", db_name)
database_exists = os.path.exists(db_path)
if database_exists:
    os.remove(db_path)

db = TinyDB(db_path)
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


def find_forms_by_fields(*args) -> list[dict]:
    q = forms_table.search(Query().form_fields.test(lambda x: set(args).issubset(set(x))))
    return q

def add_types(form: dict) -> dict:
    updated_form = {"form_name": form["form_name"], "form_fields": {}}
    for field in form["form_fields"]:
        updated_form["form_fields"][field] = fields_types[field] 
    return updated_form

# q = find_forms_by_fields("name")[0]
# print(q)
# q = add_types(q)
# print(q)
        

