from werkzeug.security import safe_str_cmp
from flask_jwt import JWT, jwt_required, current_identity
from peewee import *
from .ingredients import getingredients
from flask import request
from flask_api import FlaskAPI, status
from playhouse.flask_utils import FlaskDB
app = FlaskAPI(__name__)
db_wrapper = FlaskDB(app, 'sqlite:///my_app.db')
from .models import *


app.config.from_object(__name__)
app.config["SECRET_KEY"] = "ligma"


def authenticate(username, password):
    user = User.get_or_none(username=username)
    if user is None:
        return None
    if user.verify_password(password):
        return user
    else:
        return None


def identity(payload):
    """ also returns user """
    return User.get_or_none(id = payload["identity"])


jwt = JWT(app, authenticate, identity)


@app.route("/", methods=["GET"])
@jwt_required()
def root():
    print(current_identity)
    return []


@app.route("/ingredients/<string:key>/", methods=["GET"])
def ingredients(key):
    ingredients = getingredients(key)
    return {
        "ingredients": ingredients
    }


@app.route("/user/new", methods=["POST"])
def new_user():
    """
        once again, fucking self explanatory
        request body should look like this:
        {
            username: suck,
            email: my,
            password: dick
        }
    """
    user = User.create(
        username=request.data["username"],
        email=request.data["email"]
    )
    user.set_password(request.data["password"])
    user.save()
    return [], status.HTTP_201_CREATED


if __name__ == "__main__":

    app.run(debug=True)
