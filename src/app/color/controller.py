from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource, fields
from flask.wrappers import Response
from typing import List

from .schema import ColorSchema
from .service import ColorService
from .model import Color

api = Namespace("Color", description="Get all, a single or insert a new one")

# Model required by flask_restplus for expect
item = api.model('Color', {
    'color': fields.String('color name',description='e.g. red'),
    'value': fields.String('color hex code',description='e.g. #f00'),
})

@api.route("/")
class ColorResource(Resource):
    """Colors"""

    @api.response(200, 'Success')
    def get(self) -> List[Color]:
        """Retrieve the whole list of colors"""

        resp = ColorService.get_all()             
        return {'result':resp.get('result'),'success':resp.get('success')},resp.get('code')


    @api.expect(item)
    @api.response(201, 'Created')
    @api.response(409, 'Conflict')
    @api.response(400, 'Bad Request')
    @api.doc(description="Must be a valid color name and standard hex digit value")    
    def post(self) -> Color:
        """Insert a new color into the list"""
        
              
        resp = ColorService.create(request.get_json())        
        return {'message':resp.get('message'),'success':resp.get('success')},resp.get('code')



@api.route("/<color>")
@api.param("color", "Type a valid color name available in the database")
class ColorNameResource(Resource):
    
    @api.response(200, 'Success')
    @api.response(404, 'Not Found')
    def get(self, color) -> Color:
        """Get Single Color"""

        resp = ColorService.find_by_color(color)  
        if resp.get('success'):
            return {'result':resp.get('result'),'success':resp.get('success')},resp.get('code')
        else:
            return {'message':resp.get('result'),'success':resp.get('success')},resp.get('code')


