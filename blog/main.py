from fastapi import FastAPI
from . import schemas, models
from .database import engine

app = FastAPI()

# this below line means that on reload, create all the tables
models.Base.metadata.create_all(engine)

@app.post('/blog')
def create(request: schemas.Blog):
    return request