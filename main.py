from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return 'heyy'


@app.get('/about')
def about():
    return {'data': {'about page'}}


@app.get('/blog/{id}')
def blog(id : int):
    return {'data': id}


@app.get('/blog')
def blog(limit, published : bool):
    
    if published:
        return {'data': f'{limit} published fetched from the db'}
    else:
        return {'data': f'{limit} fetched from the db'}


@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': {'1', '2'}}


