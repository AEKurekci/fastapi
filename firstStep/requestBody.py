from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


app = FastAPI()


@app.post("/items/")
async def createItem(item: Item):
    itemDict = item.dict()
    if itemDict.tax:
        newPrice = itemDict.price + itemDict.tax
        itemDict.update({"priceWithTax": newPrice})
    return itemDict

