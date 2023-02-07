from fastapi import APIRouter

from models.answer import Answer

router = APIRouter()


@router.post('/')
async def add_answer(answer: Answer):
    await answer.save()
    return answer

@router.get('/')
async def list_answer():
    return await Answer.objects.all()

# @app.get('/item/valor_total')
# def get_valor_total():
#     # total = sum([item.valor * item.quantidade for item in banco_de_dados])

#     total = 0.0
#     for item in banco_de_dados:
#         total = item.valor * item.quantidade

#     return {'valor_total': total}