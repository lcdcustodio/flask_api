from app.color.model import Color
from flask_sqlalchemy import SQLAlchemy


def test_color_create(color: Color):
    assert color

def test_Color_retrieve(color: Color, db: SQLAlchemy):
    db.session.add(color)
    db.session.commit()
    s = Color.query.first()

    assert s.__dict__ == color.__dict__
