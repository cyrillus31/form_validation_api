from pymongo import MongoClient

from database.forms import forms


client: MongoClient = MongoClient()

db = client["forms"]

result = db.forms.insert_many(forms)

print(result)
