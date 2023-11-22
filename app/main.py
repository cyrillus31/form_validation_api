from typing import Optional
import json
import os

from fastapi import FastAPI, Request, Form

from services import evaluate_form
from database.db import db_path

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Welcome! This is the page of a project by Kirill Fedtsov (kirill.olegovich31@gmail.com). Use the following endpoint: /get_form"}


@app.get("/get_form")
async def get_form():
    with open(db_path) as json_file:
        json_data = json.load(json_file)
    return {"message": "POST the form fields to the endpoint", "known forms": json_data}
    

@app.post("/get_form")
async def get_form(request: Request):
    data = await request.form()
    response = evaluate_form(dict(data))
    return response
