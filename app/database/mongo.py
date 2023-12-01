from pymongo import MongoClient

from database.forms import forms


client: MongoClient = MongoClient(host="mongo")

db = client["forms_database"]
amount_forms = db.forms.count_documents({})
if not amount_forms:
    db.forms.insert_many(forms)


def find_forms_by_fields(*args) -> list[dict]:
    result = db.forms.find()
    return [form for form in result if set(form["form_fields"].keys()).issubset(set(args))] 
