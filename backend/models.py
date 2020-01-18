from .app import db_wrapper
from peewee import *

import datetime


class User(db_wrapper.Model):
    """
        user model, really fucking self explanatory
    """
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField(unique=True)


class EmissionsEntry(db_wrapper.model):
    """
        Individual emissions entries, must be linked to a user and is used for storing each individual instance
        a user consumes something.
    """
    user = ForeignKeyField(User, backref="entries", null=False)
    barcode = CharField(null=False)
    submitted = DateTimeField(default=datetime.datetime.now)
    ingredients = TextField(null=False)
    total_emissions = FloatField(null=False)
    emissions_per_kg = FloatField(null=False)
    weight = FloatField()


class EmissionsList(db_wrapper.Model):
    """
        Used for storing the per kg emissions for each barcode, to save from duplicate computation.
    """
    barcode = CharField(null=False)
    last_updated = DateTimeField(default=datetime.datetime.now)
    emissions_per_kg = FloatField(null=False)
    ingredients = TextField(null=False)
