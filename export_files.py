import os

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

path = "/home/nathalia/Documents/python/intro-fastapi"


@app.get("/")
def index():
    return {"message": "Hello World"}


@app.get("/dog", responses={200: {"description": "A picture of a dog."}})
def dog():
    file_path = os.path.join(path, "files/dog.jpg")
    if os.path.exists(file_path):
        return FileResponse(
            file_path,
            media_type="image/jpeg",
            filename="dog.jpg"
        )

    return {"error": "File not found!"}
