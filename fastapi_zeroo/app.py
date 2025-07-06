from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zeroo.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundinho!'}


@app.get('home', status_code=HTTPStatus.OK, response_model=Message)
def primeira_rota():
    return {'message': 'Meu teste'}


@app.get('/teste-html', response_class=HTMLResponse)
def html():
    return """
    <html>
        <head>
            <title> Estou tentanto</title>
            <body>
                <h1>O CAMIHO SÓ É DIFICIL PRA QUEM DESISTE NA METADE!!</h1>
            </body>
        </head>
    </html> """
