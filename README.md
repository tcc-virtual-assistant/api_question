# API de respostas

## Descrição:
A API tem o objetivo de fornecer respostas de perguntas relacionadas a empresa. Assim facilitando o processo de CRUD e possibilitando que a refaturação do código seja feita de uma forma mais dinámica e fácil.

## Tecnologias:
### fastAPI
> FastAPI é uma biblioteca web Python para desenvolvimento de API (Application Programming Interface) rápido e eficiente. Ele é baseado no framework Starlette e utiliza o gerenciador de dependências asyncio para fornecer alta performance e capacidade de escalabilidade.
> Além disso, FastAPI é fácil de aprender e usar, com uma sintaxe clara e concisa que permite aos desenvolvedores criarem rapidamente aplicações avançadas.

**Algumas das principais características do FastAPI incluem:**
- Documentação automática
- Suporte para requisições assíncronas

### Uvicorn:
> Uvicorn é um servidor de aplicativos web de alta performance baseado em asyncio, escrito em Python. Ele é projetado especificamente para trabalhar com aplicativos web construídos com a biblioteca FastAPI, mas também é compatível com outras bibliotecas baseadas em asyncio, como Starlette.
> Uvicorn é fácil de usar e oferece recursos avançados, como suporte para o protocolo HTTP/2, gerenciamento de subprocessos e carregamento de configurações a partir de arquivos. Além disso, ele é altamente escalável e pode lidar com muitas requisições ao mesmo tempo, tornando-o uma opção popular para aplicativos web de alta performance.
> Em resumo, Uvicorn é uma ótima escolha para executar aplicativos web construídos com bibliotecas asyncio no Python, oferecendo alta performance, escalabilidade e recursos avançados.

## Comandos:
Instalação da boblioteca fastAPI:
```
pip install fastapi
```
Instalação da boblioteca uvicorn:
```
pip install uvicorn[standard]
```
Instalação das bibliotecas por requirements:
```
pip install -r requirements.txt
```
Instalação da bibliteca para banco de dados:
```
pip install ormar[sqlite]
```
Rodar o projeto no localhost: 
```
uvicorn main:app --reload
```