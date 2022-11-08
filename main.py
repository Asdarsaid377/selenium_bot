from typing import Union

import uvicorn
from fastapi import FastAPI
from Bot import MyBot

app = FastAPI()


@app.get("/")
def read_root():
    MyBot()
    return {"Scrapping Is Running In The Background",MyBot()}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
