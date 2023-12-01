from fastapi import FastAPI, Request

from services import evaluate_form
from database.mongo import db 

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Welcome! This is the page of a project by Kirill Fedtsov (kirill.olegovich31@gmail.com). Use the following endpoint: /get_form"}


@app.get("/get_form")
async def get_information():
    forms_in_database = [form for form in db.forms.find({}, projection={"form_name": 1, "form_fields": 1, "_id": 0})]
    return {"message": "POST the form fields to the endpoint", "known forms": forms_in_database}
    

@app.post("/get_form")
async def get_form(request: Request):
    data = await request.form()
    response = evaluate_form(dict(data))
    return response
