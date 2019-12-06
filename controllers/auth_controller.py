from flask import Flask, Blueprint, render_template, request, redirect, Response
from flask_jwt_extended import create_access_token, jwt_required, get_raw_jwt
from models.user_model import Users
from services.auth_services import create_user
# from services import bcrypt
# from app import app


auth_blueprint = Blueprint('auth_api', __name__)


#'''register auth blueprint with prefix '/auth' so that auth_controller works'''
@auth_blueprint.route('/login', methods=['POST'])
def login():
    return 'login route'

@auth_blueprint.route('/register', methods=['POST'])
def register():
    # if request.method == "POST":
    #     return "Post Hit"
    body = request.json
    if body:
    # return Response("something", 200)
        try:
            return create_user(body['username'], body['email'], body['password'])
        except Exception as e:
            return str(e), 400
        return {'message': 'Thank you for registering to PennyPinchers!'}


@auth_blueprint.route('/user_details', methods=['POST'])
def user_details():
    return 'user details'