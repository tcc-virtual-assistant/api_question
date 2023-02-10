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

### Ormar:
> Ormar é uma biblioteca de banco de dados ORM (Object-Relational Mapping) para Python. Ele permite o acesso e manipulação de dados em bancos de dados relacionais, como MySQL, PostgreSQL e SQLite, usando o Python como linguagem de programação.
> Com Ormar, é possível definir modelos de dados em Python que correspondem a tabelas no banco de dados, e então usar esses modelos para realizar operações CRUD (Create, Read, Update, Delete). Isso significa que não é preciso escrever código SQL manualmente, e sim trabalhar com objetos Python para manipular dados.
> Ormar é fácil de usar e oferece recursos avançados, como suporte a transações, consultas avançadas e relacionamentos entre tabelas.

### PyTest:
> Pytest é uma biblioteca de teste de unidade para Python. Ele permite escrever testes de unidade de maneira eficiente e organizada, e oferece uma série de recursos avançados para testar aplicativos Python.
> Com Pytest, é possível escrever testes de unidade como funções normais, e ele fornece uma sintaxe simples e intuitiva para chamar essas funções e verificar seus resultados. Além disso, ele oferece recursos avançados como fixtures, marcadores de teste e hooks que permitem personalizar as estratégias de testes.
> Além disso, Pytest é altamente escalável e pode lidar com grandes quantidades de testes, o que o torna uma ótima opção para aplicativos de médio a grande porte. Ele também é compatível com uma ampla gama de bibliotecas e frameworks Python, como Django, Flask e Pygame.

### Pytest-asyncio:
> A biblioteca Pytest-asyncio é uma extensão para o Pytest que permite testar aplicativos assíncronos escritos com o módulo asyncio do Python. Ela fornece recursos adicionais para lidar com coroutines assíncronas e torna mais fácil escrever testes para aplicativos assíncronos.
> Com Pytest-asyncio, é possível escrever testes de unidade para coroutines assíncronos da mesma forma que escreveria testes para funções normais. Além disso, ele fornece uma série de fixtures que permitem testar coroutines assíncronas de maneira eficiente e organizada.

## Mapeamento de perguntas e respostas:
Para que o usuário da API possa se mapear e saiba em qual ID se encontra a resposta para cada pergunta já estipulada, foi realizado um mapeamento que informando ao usuário sobre a sua determinada localização:

Pergunta | Categoria | ID da resposta
:-----: | :-----: |:-----:
Quem é o presidente da planta/Bosch América Latina | colaborador | 1
Quem é o presidente/CEO da Bosch | colaborador | 2
Quem foi Robert Bosch | historia | 3
Qual é a história da Bosch | historia | 4
Onde devolvo o cracha provisório | local | 5
O que é VsDia | ferramenta de trabalho | 6
A quantos anos a Bosch está no Brasil | historia | 7
O que significa ETS | setor | 8
Quantas Bosch existem no mundo | curiosidade bosch | 9
Quantos colaboradores da Bosch existem no Brasil| curiosidade bosch | 10
O que a Bosch faz | curiosidade bosch | 11

## Comandos:

<details>
<summary>Instalação das bibliotecas separadamente</summary>

Instalação da boblioteca fastAPI:
```
pip install fastapi
```
Instalação da boblioteca uvicorn:
```
pip install uvicorn[standard]
```
Instalação da bibliteca para banco de dados:
```
pip install ormar[sqlite]
```
Instalação da bibliteca de testes:
```
pip install pytest
```
Instalação da bibliteca para teste assíncronos:
```
pip install pytest-asyncio
```

***
</details>

<br>

Instalação das bibliotecas por requirements:
```
pip install -r requirements.txt
```
Rodar o projeto no localhost: 
```
uvicorn main:app --reload
```

## End-points:

Documentação:
```
http://localhost:8000/docs#/
```
Listar todas as respostas:
```
http://localhost:8000/answer/
```
Adicionar resposta:
```
http://localhost:8000/answer/
```
Pegar uma resposta específica:
```
http://localhost:8000/answer/{resposta_id}
```
Deletar uma resposta específica:
```
http://localhost:8000/answer/{resposta_id}
```
Mudar um parâmetro de uma resposta específica:
```
http://localhost:8000/answer/{resposta_id}
```
