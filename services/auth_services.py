from models.user_model import Users


def create_user(username, email, password):
    new_user = Users(username, email, password)
    return new_user.save_user()