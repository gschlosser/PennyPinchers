from flask import Flask, Blueprint, Markup, render_template
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

labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

values = [
    967.67, 1190.89, 1079.75, 1349.19,
    2328.91, 2504.28, 2873.83, 4764.87,
    4349.29, 6458.30, 9907, 16297
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

@app.route('/bar')
def bar():
    bar_labels=labels
    bar_values=values
    return render_template('bar_chart.html', title='Bitcoin Monthly Price in USD', max=17000, labels=bar_labels, values=bar_values)

@app.route('/line')
def line():
    line_labels=labels
    line_values=values
    return render_template('line_chart.html', title='Bitcoin Monthly Price in USD', max=17000, labels=line_labels, values=line_values)

@app.route('/pie')
def pie():
    pie_labels = labels
    pie_values = values
    return render_template('pie_chart.html', title='Bitcoin Monthly Price in USD', max=17000, set=zip(values, labels, colors))


if __name__ == "__main__":
    app.run()