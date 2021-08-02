from .model import Color 
from .schema import ColorSchema

BASE_ROUTE = "color"


def register_routes(api, app, root="api/v1"):
    from .controller import api as color_api

    api.add_namespace(color_api, path=f"/{root}/{BASE_ROUTE}")
