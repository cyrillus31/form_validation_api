from pymongo import MongoClient

from forms import forms


client: MongoClient = MongoClient()

db = client["forms"]
amount_forms = db.forms.count_documents({})
if not amount_forms:
    db.forms.insert_many(forms)


def find_forms_by_fields(*args) -> list:
    result = db.forms.find({f"form_fields.{field_name}": {"$exists": "true"} for field_name in args})
    return result 

r = find_forms_by_fields("seller name", "phone number")
print([form for form in r])
