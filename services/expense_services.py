from models.expense_model import Expenses, ExpenseSchema
from datetime import datetime
from flask import jsonify, Response, Flask, request
import simplejson as json

def create_new_item(body, user):
    new_item = Expenses(
        expense_name = body['name'],
        expense_cost = body['cost'],
        expense_necessity = body['necessity'],
        expense_category = body['category'],
        user_id = user,
        date_created = datetime.utcnow(),
        last_modified = datetime.utcnow()
    )
    try:
        new_item.save()
        return jsonify({'message': 'Expense added.'})
    except Exception as e:
        return str(e), 400

def grab_user_items(user):
    x = Expenses.grab_all_items(user)
    return ExpenseSchema().dump(x, many=True)

def custom_response(res, status_code):
    return Response(
        mimetype='application/json',
        response= json.dumps(res),
        status=status_code
    )