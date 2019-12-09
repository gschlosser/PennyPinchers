from flask import Flask, Blueprint, render_template, request, redirect, Response
from flask_jwt_extended import create_access_token, jwt_required, get_raw_jwt
from models.user_model import Users
from services.auth_services import create_user
from services import bcrypt


auth_blueprint = Blueprint('auth_api', __name__)


#'''register auth blueprint with prefix '/auth' so that auth_controller works'''
@auth_blueprint.route('/login', methods=['POST'])
def login():
    body = request.json
    error=None

    check_if_user_exists = Users.query.filter_by(email=body['email']).first()
    check_if_pw_matches = bcrypt.check_password_hash(check_if_user_exists.password, body['password'])
    
    if check_if_pw_matches:
        access_token = create_access_token(check_if_user_exists.id)
        return {
            'message': 'You have logged in as ',
            'Your login token is': access_token
        }
    else: 
        return 'Incorrect password, please try again.'

@auth_blueprint.route('/register', methods=['POST'])
def register():
    # if request.method == "POST":
    #     return "Post Hit"
    if request.json:
    # return Response("something", 200)
    
        try:
            return create_user(request.json['username'], request.json['email'], bcrypt.generate_password_hash(request.json['password']).decode('utf-8'))
        except Exception as e:
            return str(e), 400
        return {'message': 'Thank you for registering to PennyPinchers!'}


@auth_blueprint.route('/user_details', methods=['POST'])
def user_details():
    return 'user details'