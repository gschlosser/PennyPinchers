from models.expense_model import Expenses, ExpenseSchema
from datetime import datetime
from flask import jsonify


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

    