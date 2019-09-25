from flask import Blueprint
from flask_restful import Api
# from restful import Api

from resources.Hello import UsersResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(UsersResource, '/')