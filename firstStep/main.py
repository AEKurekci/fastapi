from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    isOffer: bool = None

@app.get("/")
def readRoot():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def readItem(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def updateItem(item_id: int, item: Item):
    return {"item_name:": item.name, "item_id": item_id}
