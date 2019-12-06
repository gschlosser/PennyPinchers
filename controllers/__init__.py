from flask_jwt_extended import JWTManager

jwt = JWTManager()
from .auth_controller import auth_blueprint