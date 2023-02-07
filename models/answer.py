import ormar

from config import database, metadata

class Answer(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = "respostas"

    id: int = ormar.Integer(primary_key = True)
    response: str = ormar.String(max_length=10000)
    categoria: str = ormar.String(max_length=100)
