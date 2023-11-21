from typing import Optional

from fastapi import FastAPI, Request, Form

from services import evaluate_form

app = FastAPI()


@app.get("/")
def index():
    return "<h1>Welcome</h1>"


# @app.post("/get_form")
# def get_form(request: Request):
#     query_params = request.query_params
#     params = dict()
#     for param in query_params:
#         params[param] = query_params[param]
#     NewForm(**params)
#     return "Who wants what?"

@app.post("/get_form")
async def get_form(request: Request):
    data = await request.form()
    response = evaluate_form(dict(data))
    return response
