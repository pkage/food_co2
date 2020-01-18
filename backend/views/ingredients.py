from app import *

from ..ingredients import getingredients

from flask import request
from flask_api import status, exceptions

@app.route("/ingredients/<int:barcode>", methods = ["GET"])
def ingredients(barcode):
    ingredients = getingredients(barcode)
    return {
        "ingredients" : ingredients
    }