from typing import Optional

from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
def index():
    return "<h1>Welcome</h1>"


@app.get("/get_form")
def get_form(request: Request):
    query_params = request.query_params
    params = dict()
    for param in query_params:
        params[param] = query_params[param]
    return params 
