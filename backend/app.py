from flask_api import FlaskAPI

from ingredients import getingredients

app = FlaskAPI(__name__)


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
