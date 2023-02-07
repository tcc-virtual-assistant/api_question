import ormar
import re
from pydantic import validator
from sqlalchemy.sql.expression import table

from config import database, metadata

class Answer(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = "respostas"

    id: int = ormar.Integer(primary_key = True)
    response: str = ormar.String(max_length=10000)
    categoria: str = ormar.String(max_length=100)

    # @validator('sigla')
    # def valida_formatacao_sigla(cls, v):
    #     if not re.compile('^[A-Z]{4}[0-9]{1,2}$').match(v):
    #         raise ValueError('A sigla do papel é inválida!')
    #     return v