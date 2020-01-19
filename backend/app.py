from werkzeug.security import safe_str_cmp
from flask_jwt import JWT, jwt_required, current_identity
from peewee import *
from backend.ingredients import getingredients
from .product import containspalm, getname
from backend.carbon import get_carbon_footprint, get_car_footprint
from backend.train import calctrainfromdistance
from backend.plane import calcflightfromdistance
from flask import request
from flask_api import FlaskAPI, status
from playhouse.flask_utils import FlaskDB
from flask_cors import CORS
import datetime
app = FlaskAPI(__name__)
CORS(app)
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


@app.route("/cars/emissions", methods=["GET"])
@jwt_required()
def car_emissions():
    footprint = get_car_footprint(request.args.get("model"), request.args.get("distance"))
    EmissionsEntry.create(
        user=current_identity.id,
        barcode="car",
        min_total_emissions=footprint,
        max_total_emissions=footprint,
        min_emissions_per_kg=footprint/int(request.args.get("distance")),
        max_emissions_per_kg=footprint/int(request.args.get("distance")),
        weight=int(request.args.get("distance")),
        ingredients="",
        name=request.args.get("model"),
        palm_oil=False
    )
    return {
        "emissions": footprint
    }

@app.route("/trains/emissions", methods=["GET"])
@jwt_required()
def train_emissions(): 
    footprint = calctrainfromdistance(request.args.get("distance"))
    EmissionsEntry.create(
        user=current_identity.id,
        barcode="train",
        min_total_emissions=footprint,
        max_total_emissions=footprint,
        min_emissions_per_kg=footprint/int(request.args.get("distance")),
        max_emissions_per_kg=footprint/int(request.args.get("distance")),
        weight=int(request.args.get("distance")),
        ingredients="",
        name=request.args.get("Train"),
        palm_oil=False
    )
    return {
        "emissions": footprint
    }

@app.route("/planes/emissions", methods=["GET"])
@jwt_required()
def plane_emissions(): 
    footprint = calcflightfromdistance(request.args.get("distance"))
    EmissionsEntry.create(
        user=current_identity.id,
        barcode="plane",
        min_total_emissions=footprint,
        max_total_emissions=footprint,
        min_emissions_per_kg=footprint/int(request.args.get("distance")),
        max_emissions_per_kg=footprint/int(request.args.get("distance")),
        weight=int(request.args.get("distance")),
        ingredients="",
        name=request.args.get("Plane"),
        palm_oil=False
    )
    return {
        "emissions": footprint
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
            name=getname(barcode),
            palm_oil=containspalm(barcode)
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
            name=getname(barcode),
            palm_oil=containspalm(barcode)

        )
        response = emmissions_entry.to_dict()
        del response["created_at"]
        EmissionsList.create(
            barcode=barcode,
            min_emissions_per_kg=emissions["min_per_kg"],
            max_emissions_per_kg=emissions["max_per_kg"],
            ingredients=str(ingredients),
            weight=emissions["weight_in_kg"],
            name=getname(barcode),
            palm_oil=containspalm(barcode)
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


@app.route("/user/daily", methods=["GET"])
@jwt_required()
def daily_totals():
    dates = {}
    for entry in current_identity.entries:
        if entry.submitted.date().isoformat() in dates:
            dates[entry.submitted.date().isoformat()].append(entry.to_dict())
        else:
            dates[entry.submitted.date().isoformat()] = [entry.to_dict()]

    res = {}
    for date in dates:
        res[date] = {
            "max": sum([entry["max_total_emissions"] for entry in dates[date]]),
            "min": sum([entry["min_total_emissions"] for entry in dates[date]]),
            "count": len(dates[date])
        }
    return res


@app.route("/user/new", methods=["POST"])
def new_user():
    """
        once again, f*****g self explanatory
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
