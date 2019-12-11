from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from models import db
from controllers import auth_blueprint, expense_blueprint, auth_controller, expense_controller, jwt
from services.auth_services import create_user
from services import bcrypt



app = Flask(__name__)


app.config.from_object('config.Development')

db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)


@app.route('/', methods = ['GET'])
def home():
    return 'Welcome Home!'

app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(expense_blueprint, url_prefix='/expenses')

if __name__ == "__main__":
    app.run()