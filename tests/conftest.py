import pika
import pytest

from app import broker, create_app
from app.db import db


@pytest.fixture
def app():
    app = create_app("testing")
    return app


@pytest.fixture(scope="function")
def task_conn(app):
    with app.app_context():
        conn = broker.create_conn()
    yield conn


@pytest.fixture(scope="function")
def database(app):
    with app.app_context():
        db.drop_all()
        db.create_all()
    yield db
