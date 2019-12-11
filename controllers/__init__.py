from flask_jwt_extended import JWTManager

jwt = JWTManager()
blacklist = set()

from .auth_controller import auth_blueprint
from .expense_controller import expense_blueprint