from .app import db_wrapper
from peewee import *  # noqa

from .product import containspalm


import datetime
import hashlib


class User(db_wrapper.Model):
    """
        user model, really fucking self explanatory
    """
    id = PrimaryKeyField(unique=True)
    username = CharField(unique=True)
    email = CharField(unique=True)
    password_hash = CharField(null=True)

    def set_password(self, password):
        self.password_hash = str(hashlib.sha256(password.encode('utf-8')).hexdigest())

    def verify_password(self, password):
        return self.password_hash == str(hashlib.sha256(password.encode('utf-8')).hexdigest())


User.create_table()


class EmissionsEntry(db_wrapper.Model):
    """
        Individual emissions entries, must be linked to a user and is used for storing each individual instance
        a user consumes something.
    """
    user = ForeignKeyField(User, backref="entries", null=False)
    barcode = CharField(null=False)
    submitted = DateTimeField(default=datetime.datetime.now)
    ingredients = TextField(null=False)
    min_total_emissions = FloatField(null=False)
    max_total_emissions = FloatField(null=False)
    min_emissions_per_kg = FloatField(null=False)
    max_emissions_per_kg = FloatField(null=False)
    weight = FloatField()
    name = CharField()

    def to_dict(self):
        return {
            "barcode": self.barcode,
            "ingredients": [el.strip(" []' ") for el in self.ingredients.split(",")],
            "min_emissions_per_kg": self.min_emissions_per_kg,
            "max_emissions_per_kg": self.max_emissions_per_kg,
            "min_total_emissions": self.min_emissions_per_kg*self.weight,
            "max_total_emissions": self.max_emissions_per_kg*self.weight,
            "weight_in_kg": self.weight,
            "palm_oil": containspalm(self.barcode),
            "created_at": self.submitted,
            "name": self.name
        }


EmissionsEntry.create_table()


class EmissionsList(db_wrapper.Model):
    """
        Used for storing the per kg emissions for each barcode, to save from duplicate computation.
    """
    barcode = CharField(null=False)
    last_updated = DateTimeField(default=datetime.datetime.now)
    min_emissions_per_kg = FloatField(null=False)
    max_emissions_per_kg = FloatField(null=False)
    ingredients = TextField(null=False)
    weight = FloatField(null=False)
    name = CharField()

    def to_dict(self):
        return {
            "barcode": self.barcode,
            "ingredients": [el.strip(" []' ") for el in self.ingredients.split(",")],
            "min_emissions_per_kg": self.min_emissions_per_kg,
            "max_emissions_per_kg": self.max_emissions_per_kg,
            "min_total_emissions": self.min_emissions_per_kg*self.weight,
            "max_total_emissions": self.max_emissions_per_kg*self.weight,
            "weight_in_kg": self.weight,
            "palm_oil": containspalm(self.barcode),
            "name": self.name
        }


EmissionsList.create_table()
