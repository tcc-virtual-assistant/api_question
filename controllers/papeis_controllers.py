from fastapi import APIRouter

from models.papel import Papel

router = APIRouter()

banco_de_dados = []

@router.post('/')
def add_item(item: Papel):
    banco_de_dados.append(item)
    return item

@router.get('/')
def list_item():
    return banco_de_dados

# @app.get('/item/valor_total')
# def get_valor_total():
#     # total = sum([item.valor * item.quantidade for item in banco_de_dados])

#     total = 0.0
#     for item in banco_de_dados:
#         total = item.valor * item.quantidade

#     return {'valor_total': total}