from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
def index():
    return 'heyy'


@app.get('/about')
def about():
    return {'data': {'about page'}}


@app.get('/blog/{id}')
def blog(id: int):
    return {'data': id}


@app.get('/blog')
def blog(limit, published: bool):
    if published:
        return {'data': f'{limit} published fetched from the db'}
    else:
        return {'data': f'{limit} fetched from the db'}


@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': {'1', '2'}}

########### Request Body Using Post ###########


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f'Blog is created by {request.title}'}


import uvicorn

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)