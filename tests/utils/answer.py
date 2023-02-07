def create_answer_valido():
    return {
        'id' : 0,
        'response' : 'string',
        'categoria' : 'string'
    }

def create_answer_invalido(campos = ['sigla']):
    answer_invalido = {
        'id' : 0,
        'response' : 'string',
        'categoria' : 'string'
    }

    if 'sigla' in campos_invalidos:
        answer_invalido['sigla'] = 'AAAAAAAA'

    return answer_invalido