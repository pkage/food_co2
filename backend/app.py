from flask_api import FlaskAPI
from peewee import *
from playhouse.flask_utils import FlaskDB

from ingredients import getingredients

DATABASE = "sqlite://db.sqlite3"

app = FlaskAPI(__name__)
app.config.from_object(__name__)

db_wrapper = FlaskDB(app)


@app.route("/", methods=["GET"])
def root():
    return {"foo": "bar"}


@app.route("/ingredients/<string:key>/", methods=["GET"])
def ingredients(key):
    ingredients = getingredients(key)
    return {
        "ingredients": ingredients
    }


if __name__ == "__main__":
    app.run(debug=True)
