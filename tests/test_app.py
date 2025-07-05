from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zeroo.app import app


def test_root_deve_retornar_ola_mundo():
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
