from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# Rota Raiz


@app.get("/")
async def root():
    return {"message": "Hello World"}

fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"}
]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

# Query parameter type conversion + Optional parameters


@app.get("/items/{item_id}")
async def read_item_by_id(
    item_id: str, q: Optional[str] = None, short: bool = False
):

    item = {"item_id": item_id}

    if q:
        item.update({"q": q})

    if not short:
        item.update(
            {
                "description":
                "This is an amazing item that has a long description"
            }
        )

    return item


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

# Multiple path and query parameters


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}

    if q:
        item.update({"q": q})

    if not short:
        item.update(
            {
                "description":
                "This is an amazing item that has a long description"
            }
        )
    return item
