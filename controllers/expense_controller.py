from flask import Blueprint
from flask import Flask, request
from services.expense_services import create_new_item, Expenses, grab_user_items, custom_response
from flask_jwt_extended import JWTManager, get_jwt_identity, jwt_required


expense_blueprint = Blueprint('expense_api', __name__)


@expense_blueprint.route('/new_item', methods=['POST'])
@jwt_required
def new_item():
    body = request.json
    user = get_jwt_identity()
    try:
        return create_new_item(body, user)
    except Exception as e:
        return str(e), 400

@expense_blueprint.route('/view_items', methods=['GET'])
@jwt_required
def view_items():
    user = get_jwt_identity()
    user_expenses = grab_user_items(user)
    return custom_response(user_expenses, 200)

# @expense_blueprint.route('/view_trends', methods=['GET', 'POST'])
# def view_trends():
    #pie chart for single days up to a week
    #linear graph for anything more than a week
    #use mpld3 to embed matplotlib graph in web page