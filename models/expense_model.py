from marshmallow import Schema, fields
from . import db, user_model
from datetime import datetime
from flask import jsonify

class Expenses(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    expense_name = db.Column(db.String(40), nullable=False)
    expense_cost = db.Column(db.Float(), nullable=False)
    expense_necessity = db.Column(db.String(15), nullable=False)
    expense_category = db.Column(db.String(20), nullable=False)
    date_created = db.Column(db.DateTime)
    last_modified = db.Column(db.DateTime)

    def __init__(self, user_id, expense_name, expense_cost, expense_necessity, expense_category, date_created, last_modified):
        self.user_id = user_id
        self.expense_name = expense_name
        self.expense_cost = expense_cost
        self.expense_necessity = expense_necessity
        self.expense_category = expense_category
        self.date_created = date_created
        self.last_modified = last_modified

    def save(self):
        db.session.add(self)
        db.session.commit()
        return jsonify({'message':'Expense added'})

class ExpenseSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    expense_name = fields.Str(required=True)
    expense_cost = fields.Float(required=True)
    expense_necessity = fields.Str(required=True)
    expense_category = fields.Str(required=True)
    date_created = fields.DateTime(dump_only=True)
    last_modified = fields.DateTime(dump_only=True)
    