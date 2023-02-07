from fastapi.testclient import TestClient
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