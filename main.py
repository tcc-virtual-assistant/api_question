from typing import Optional
from fastapi import FastAPI, Header, Response, Cookie
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    descricao: str
    valor: float
    quantidade: int

app = FastAPI()

banco_de_dados = []

@app.post('/item')
def add_item(item: Item):
    banco_de_dados.append(item)
    return item

@app.get('/item')
def list_item():
    return banco_de_dados

@app.get('/item/valor_total')
def get_valor_total():
    # total = sum([item.valor * item.quantidade for item in banco_de_dados])

    total = 0.0
    for item in banco_de_dados:
        total = item.valor * item.quantidade

    return {'valor_total': total}