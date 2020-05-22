from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


class Item(BaseModel):
    name: str
    price: float
    isOffer: bool = None


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def readItem(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def updateItem(item_id: int, item: Item):
    return {"item_name:": item.name, "item_id": item_id}


@app.get("/model/{modelName}")
async def getModel(modelName: ModelName):
    if modelName == ModelName.alexnet:
        return {"model_name ": modelName, "message ": "Machine Learning FTW!"}
    if modelName.value == ModelName.lenet:
        return {"model_name ": modelName, "message ": "LeCNN all the images"}
    return {"model_name ": modelName, "message ": "Have some residuals"}
