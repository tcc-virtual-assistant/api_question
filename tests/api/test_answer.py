import asyncio

from fastapi.testclient import TestClient
from models.answer import Answer
from tests.utils.answer import create_answer_valido, create_answer_invalido

def test_criar_answer(client: TestClient) -> None:
    body = create_answer_valido()
    response = client.post('/answer/', json = body)
    content = response.json()
    assert response.status_code == 200
    assert content['categiria'] == body['categoria']

def test_criar_answer(client: TestClient) -> None:
    body = create_answer_invalido(['sigla'])
    response = client.post('/answer/', json = body)
    content = response.json()
    assert response.status_code == 422

def test_obtem_um_answer_por_id(client: TestClient) -> None:
    atributos = create_answer_valido()
    answer = Answer(**atributos)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(answer.save())

    response = client.get(f'/answer/{answer.id}')
    content = response.json()

    assert response.status_code == 200
    assert content['categoria'] == answer.categoria

def test_obtem_papel_inexistente_por_id(client: TestClient) -> None:
    response = client.get(f'/answer/1')
    content = response.json()

    assert response.status_code == 404
    assert content['mensagem'] == 'Entidade não encontrada'