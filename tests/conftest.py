import os
DATABASE_URL = 'sqlite:///testedb.sqlite'
os.environ['DATABASE_URL'] = DATABASE_URL
os.environ['TEST_DATABASE'] = 'true'

from fastapi.testclient import TestClient
import pytest

from main import app
from cria_tabelas import config_banco

@pytest.fixture(scope='function')
def client() -> Generator:
    config_banco(DATABASE_URL)
    with TestClient(app) as c:
        yield c