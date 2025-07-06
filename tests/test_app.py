from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zeroo.app import app


def read_root():
    # ARRANGUE
    client = TestClient(app)
    # ACT
    response = client.get('/')
    # aSSERT
    assert response.json() == {'message': 'Olá Mundinho!'}
    assert response.status_code == HTTPStatus.OK

    # Esse teste tem 3 etapas (AAA)
    # A: Arrangue - Arranjo - Organizar
    # A: act      - Executa a coisa (o SUT) - Agir
    # A: Assert   - Garanta que é A É A


def primeira_rota():
    client = TestClient(app)

    response = client.get('home')

    assert response.json == {'message': 'Meu teste'}
    assert response.status_code == HTTPStatus.OK


def html():
    client = TestClient(app)

    response = client.get('/teste-html')
    assert response.status_code == HTTPStatus.OK
    assert (
        '<h1>O CAMIHO SÓ É DIFICIL PRA QUEM DESISTE NA METADE!!</h1>'
        in response.text
    )
