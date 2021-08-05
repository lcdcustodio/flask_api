from app import db
from flask import request, json, jsonify
from .schema import ColorSchema

from colour import Color as ColorCheck
import sys

from sqlalchemy.exc import IntegrityError

from typing import List
from .model import Color

color_schema = ColorSchema(many=True)

class ColorService:
    @staticmethod
    def get_all() -> List[Color]:

        result = {}
        result.update({'result': color_schema.dump(Color.query.all())})
        result.update({'success': True})
        result.update({'code': 200})   

        return result
    
    @staticmethod
    def find_by_color(color) -> Color:

        result = {}


        if Color.query.filter_by(color=color).first():
           result.update({'result': [Color.query.filter_by(color=color).one().json()]})
           result.update({'success': True})
           result.update({'code': 200})   
           return result      

        result.update({'result': 'Color \'%s\' not found' % color})
        result.update({'success': False})
        result.update({'code': 404})
        return result


    @staticmethod
    def create(data) -> Color:
    
        valid = Validation(data['color'],data['value'])        

        status, msg = valid.check_color()

        if not status:
            result = {}
            result.update(msg)
            result.update({'success': False})
            result.update({'code': 400})
            return result

        status, msg = valid.check_hex()

        if not status:
            result = {}
            result.update(msg)
            result.update({'success': False})
            result.update({'code': 400})
            return result

        
        try:
            db.session.add(Color(color=data['color'], value=data['value']))
            db.session.commit()
            result = {}
            result.update({'message': 'Color \'%s\' added!' % data['color']})
            result.update({'success': True})
            result.update({'code': 201})
            return result

        except IntegrityError:
            db.session.rollback()
            result = {}
            result.update({'message': 'Color \'%s\' already exist!' % data['color']})
            result.update({'success': False})
            result.update({'code': 409})
            return result

class Validation():

    def __init__(self, color, value): 
        self.color = color
        self.value = value

    def check_color(self):    

        try:
            ColorCheck(self.color)
            return True, {'message':'OK'}
        except ValueError as e:            
            return False, {'message':str(e)}            
            
    def check_hex(self):

        try: 

            ColorCheck(self.value)

            if ColorCheck(self.color) == ColorCheck(self.value):

                return True, {'message':'OK'}
            else:
                return False, {'message':'Color \'%s\' and hex code \'%s\' mismatch' % (self.color, self.value)}


        except AttributeError as e:            
            return False, {'message':'Value \'%s\' is not web format. Need 3 or 6 hex digit' % self.value}

        except ValueError as e:            
            return False, {'message':'Value \'%s\' is not web format. Need 3 or 6 hex digit' % self.value}








