from sqlalchemy import Integer, Column, String
from app import db


class Color(db.Model):

    __tablename__ = "color"

    id = db.Column(Integer(), primary_key=True)
    color = db.Column(String(80), nullable=False, unique=True)
    value = db.Column(String(80), nullable=False, unique=True)  

    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __repr__(self):
        return f'Color(color={self.color}, value={self.value})'

    def json(self):
        return {'color': self.color, 'value': self.value}   
