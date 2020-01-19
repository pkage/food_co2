from werkzeug.security import safe_str_cmp
from flask_jwt import JWT, jwt_required, current_identity
from peewee import *
from .ingredients import getingredients
from backend.carbon import get_carbon_footprint
from flask import request
from flask_api import FlaskAPI, status
from playhouse.flask_utils import FlaskDB
app = FlaskAPI(__name__)
db_wrapper = FlaskDB(app, 'sqlite:///my_app.db')
from .models import *  # noqa


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
    return User.get_or_none(id=payload["identity"])


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


@app.route("/emissions/<string:barcode>/", methods=["GET"])
@jwt_required()
def emissions(barcode):
    cached_emissions_entry = EmissionsList.get_or_none(barcode=barcode)
    if cached_emissions_entry is not None:
        emissions = {
            "min": cached_emissions_entry.min_emissions_per_kg,
            "max": cached_emissions_entry.max_emissions_per_kg,
            "barcode": cached_emissions_entry.barcode,
            "ingredients": cached_emissions_entry.barcode
        }
    else:
        emissions = get_carbon_footprint(barcode)
        EmissionsEntry.create(
            user=current_identity.id,
            barcode=barcode,
            min_total_emissions=emissions["min_per_kg"]*emissions["weight_in_kg"],
            max_total_emissions=emissions["max_per_kg"]*emissions["weight_in_kg"],
            min_emissions_per_kg=emissions["min_per_kg"],
            max_emissions_per_kg=emissions["max_per_kg"],
            weight=emissions["weight_in_kg"],
            ingredients=str(getingredients(barcode))
        )
        EmissionsList.create(
            barcode=barcode,
            min_emissions_per_kg=emissions["min_per_kg"],
            max_emissions_per_kg=emissions["max_per_kg"],
            ingredients=str(getingredients(barcode))
        )
    return emissions


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
