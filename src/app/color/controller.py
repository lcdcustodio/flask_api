from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import ColorSchema
from .service import ColorService
from .model import Color

api = Namespace("Color", description="Get all, a single or insert a new one")


@api.route("/")
class ColorResource(Resource):
    """Colors"""

    @responds(schema=ColorSchema(many=True))
    def get(self) -> List[Color]:
        """Retrieve the whole list of colors"""

        return ColorService.get_all()        

    @accepts(schema=ColorSchema, api=api)
    @api.response(201, 'Created')
    @api.response(409, 'Conflict')
    @api.doc(description="Must be a valid color name and standard 3 hex digit value")    
    def post(self) -> Color:
        """Insert a new color into the list"""
        
        resp = ColorService.create(request.parsed_obj)        
        return {'message':resp.get('message'),'success':resp.get('success')},resp.get('code')



@api.route("/<color>")
@api.param("color", "Type a valid color name available in the database")
class ColorNameResource(Resource):
    
    @api.response(200, 'Success')
    @api.response(404, 'Not Found')
    def get(self, color) -> Color:
        """Get Single Color"""

        resp = ColorService.find_by_color(color)  
        return {'result':resp.get('result'),'success':resp.get('success')},resp.get('code')
