from typing import Optional
from fastapi import FastAPI, Header, Response, Cookie
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    descricao: str
    valor: float

app = FastAPI()

@app.get('/')
def read_root(user: Optional[str] = Header('indefinido')):
    return {'user' : user}

@app.get('/cookie')
def cookie(response: Response):
    response.set_cookie(key='mycookie', value='Ola Mundo')
    return {'cookie': True}

@app.get('/get-cookie')
def get_cookie(mycookie: Optional[str] = Cookie(None)):
    return {'Cookie' : mycookie}

@app.get('/items/{item_id}')
def read_item(item_id: int, b: bool, s: Optional[str] = None):
    return {'item_id' : item_id, 'string' : s, 'booleano' : b}

@app.post('/item')
def add_item(novo_item: Item, outro_item: Item):
    return novo_item, outro_item