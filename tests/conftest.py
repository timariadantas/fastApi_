import pytest
from fastapi.testclient import TestClient

from fastapi_zeroo.app import app


# A: Arrangue - Arranjo - Organizar
@pytest.fixture
def client():
    return TestClient(app)
