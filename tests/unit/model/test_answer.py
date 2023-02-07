from tests.utils.answer import create_answer_valido, create_answer_invalido
from models.answer import Answer

def test_cria_answer_valido() -> None:
    atributos = create_answer_valido()
    answer = Answer(**atributos)

def test_cria_answer_com_sigla_invalida() -> None:
    with pytest.raises(ValueError, match='A sigla do papel é invalida'):
        atributos = create_answer_invalido(['sigla'])
        answer = Answer(**atributos)