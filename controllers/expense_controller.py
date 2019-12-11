from flask import Blueprint
from flask import Flask, request
from services.expense_services import create_new_item
from flask_jwt_extended import JWTManager, get_jwt_identity


expense_blueprint = Blueprint('expense_api', __name__)


@expense_blueprint.route('/new_item', methods=['POST'])
def new_item():
    body = request.json
    user = get_jwt_identity()
    try:
        return create_new_item(body, user)
    except Exception as e:
        return str(e), 407

# @expense_blueprint.route('/view_items', methods=['GET'])
# def view_items():


# @expense_blueprint.route('/view_trends', methods=['GET', 'POST'])
# def view_trends():
    