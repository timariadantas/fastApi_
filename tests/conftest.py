from contextlib import contextmanager
from datetime import datetime

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session

from fastapi_zeroo.app import app
from fastapi_zeroo.models import table_registry


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session
    table_registry.metadata.drop_all(engine)


# função para ocultar a hoje e data quando for cadastrar dados no db
# a nivel de test
@contextmanager
def _mock_db_time(*, model, time=datetime(2025, 7, 10)):
    def fake_time_hook(mapper, connection, target):
        if hasattr(target, 'create_at'):
            target.create_at = time
        if hasattr(target, 'updated_at'):
            target.updated_at = time

    event.listen(model, 'before_insert', fake_time_hook)
    yield time
    event.remove(model, 'before_insert', fake_time_hook)


@pytest.fixture
def mock_db_time():
    return _mock_db_time
