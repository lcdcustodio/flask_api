#cmd: pytest tests/ --fixtures
import pytest
from app import create_app

from app.color.model import Color


@pytest.fixture
def app():
    """Instance of Main flask app"""
    app = create_app("test")
    return app


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def color() -> Color:
    return Color(color="blue", value="#00f")    

@pytest.fixture
def db(app):

    from app import db

    with app.app_context():
        db.drop_all()
        db.create_all()
        yield db
        db.drop_all()
        db.create_all()
        db.session.commit()    
