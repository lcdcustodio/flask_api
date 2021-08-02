from app import db
from flask import request, json, jsonify
from .schema import ColorSchema

from sqlalchemy.exc import IntegrityError

from typing import List
from .model import Color


class ColorService:
    @staticmethod
    def get_all() -> List[Color]:

        return Color.query.all()
    
    @staticmethod
    def find_by_color(color) -> Color:

        result = {}


        if Color.query.filter_by(color=color).first():
           result.update({'result': Color.query.filter_by(color=color).one().json()})
           result.update({'success': True})
           result.update({'code': 200})   
           return result      

        result.update({'result': 'Color %s not found' % color})
        result.update({'success': False})
        result.update({'code': 404})
        return result


    @staticmethod
    def get_by_id(id: int) -> Color:
        return Color.query.get(id)

    @staticmethod
    def create(data) -> Color:
    
        try:
            db.session.add(Color(color=data['color'], value=data['value']))
            db.session.commit()
            result = {}
            result.update({'message': 'Color %s added!' % data['color']})
            result.update({'success': True})
            result.update({'code': 201})
            return result

        except IntegrityError:
            db.session.rollback()
            result = {}
            result.update({'message': 'Color %s already exist!' % data['color']})
            result.update({'success': False})
            result.update({'code': 409})
            return result
