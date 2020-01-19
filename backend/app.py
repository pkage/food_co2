from werkzeug.security import safe_str_cmp
from flask_jwt import JWT, jwt_required, current_identity
from peewee import *
from .ingredients import getingredients
from .product import containspalm, getname
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
    """
        get emissions and other relevant information about a particular product.
        Responses look like this: 
        {
            "barcode": "4251097403083",
            "ingredients": ["bean"],
            "max_emissions_per_kg": 26.941587267561104,
            "min_emissions_per_kg": 4.412857142857144,
            "max_total_emissions": 26.941587267561104,
            "min_total_emissions": 4.412857142857144,
            "weight_in_kg": 1
            "palm_oil": true
        }
    """
    cached_emissions_entry = EmissionsList.get_or_none(barcode=barcode)
    if cached_emissions_entry is not None:
        response = cached_emissions_entry.to_dict()
        EmissionsEntry.create(
            user=current_identity.id,
            barcode=barcode,
            min_total_emissions=cached_emissions_entry.min_emissions_per_kg*cached_emissions_entry.weight,
            max_total_emissions=cached_emissions_entry.max_emissions_per_kg*cached_emissions_entry.weight,
            min_emissions_per_kg=cached_emissions_entry.min_emissions_per_kg,
            max_emissions_per_kg=cached_emissions_entry.max_emissions_per_kg,
            weight=cached_emissions_entry.weight,
            ingredients=cached_emissions_entry.ingredients,
            name=getname(barcode)
        )
    else:
        emissions = get_carbon_footprint(barcode)
        ingredients = getingredients(barcode)
        emmissions_entry = EmissionsEntry.create(
            user=current_identity.id,
            barcode=barcode,
            min_total_emissions=emissions["min_per_kg"]*emissions["weight_in_kg"],
            max_total_emissions=emissions["max_per_kg"]*emissions["weight_in_kg"],
            min_emissions_per_kg=emissions["min_per_kg"],
            max_emissions_per_kg=emissions["max_per_kg"],
            weight=emissions["weight_in_kg"],
            ingredients=str(ingredients),
            name=getname(barcode)
        )
        response = emmissions_entry.to_dict()
        del response["created_at"]
        EmissionsList.create(
            barcode=barcode,
            min_emissions_per_kg=emissions["min_per_kg"],
            max_emissions_per_kg=emissions["max_per_kg"],
            ingredients=str(ingredients),
            weight=emissions["weight_in_kg"],
            name=getname(barcode)
        )
    return response


@app.route("/user/entries", methods=["GET"])
@jwt_required()
def entries():
    entries = []
    for entry in current_identity.entries:
        entries.append(entry.to_dict())
    return {
        "len": len(entries),
        "products": list({e.name for e in current_identity.entries}),
        "entries": entries
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
