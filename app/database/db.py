import os

from tinydb import TinyDB


cwd = os.getcwd()
database_exists = os.path.exists(os.path.join(cwd, "database", 'db.json'))

if not database_exists:
    db = TinyDB(os.path.join(cwd, "database", 'db.json'))
    db.insert({
        "New_client_form": "Form_template_name",
        "Clients name": "text",
        "Clients phone": "phone",
        "Clients email": "email",
        "Date registered": "date",
         })



