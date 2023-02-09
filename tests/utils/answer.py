def create_answer_valido():
    return {
        'id' : 0,
        'response' : 'string',
        'categoria' : 'string'
    }

def create_answer_invalido(campos = ['categoria']):
    answer_invalido = {
        'id' : 0,
        'response' : 'string',
        'categoria' : 'string'
    }

    if 'categoria' in answer_invalido:
        answer_invalido['categoria'] = 'AAAAAAAA'

    return answer_invalido