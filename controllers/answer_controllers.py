from fastapi import APIRouter, Response
import ormar

from models.answer import Answer
from models.requests.answer_update import AnswerUpdate

router = APIRouter()


@router.post('/')
async def add_answer(answer: Answer):
    await answer.save()
    return answer

@router.get('/')
async def list_answer():
    return await Answer.objects.all()

@router.get('/{answer_id}')
async def get_answer(answer_id: int, response: Response):
    try:
        answer = await Answer.objects.get(id = answer_id)
        return answer
    except ormar.exceptions.NoMatch:
        response.status_code = 404
        return {'mensagem' : 'Entidade não encontrada'}

@router.patch('/{answer_id}')
async def path_answer(propriedades_atualizacao: AnswerUpdate, answer_id: int, response: Response):
    try:
        answer_salvo = await Answer.objects.get(id = answer_id)
        propriedades_atualizadas = propriedades_atualizacao.dict(exclude_unset=True)
        await answer_salvo.update(**propriedades_atualizadas)
        return answer_salvo
    except ormar.exceptions.NoMatch:
        response.status_code = 404
        return {'mensagem' : 'Entidade não encontrada'}

# @app.get('/item/valor_total')
# def get_valor_total():
#     # total = sum([item.valor * item.quantidade for item in banco_de_dados])

#     total = 0.0
#     for item in banco_de_dados:
#         total = item.valor * item.quantidade

#     return {'valor_total': total}