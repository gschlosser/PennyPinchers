from . import db

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(40), unique = True, nullable=False)
    email = db.Column(db.String(40), unique = True, nullable=False)
    password = db.Column(db.String(500), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def save_user(self):
        db.session.add(self)
        db.session.commit()
        return 'Welcome back!'

