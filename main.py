from fastapi import FastAPI
import uvicorn
from rotas import router

app = FastAPI()

@app.get('/')
def get_root():
    return {'mensagem': 'api de respostas bosch'}

app.include_router(router, prefix="")

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")