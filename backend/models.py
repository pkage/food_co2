from .app import db_wrapper
from peewee import *  # noqa

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
    total_emissions = FloatField(null=False)
    emissions_per_kg = FloatField(null=False)
    weight = FloatField()
EmissionsEntry.create_table()


class EmissionsList(db_wrapper.Model):
    """
        Used for storing the per kg emissions for each barcode, to save from duplicate computation.
    """
    barcode = CharField(null=False)
    last_updated = DateTimeField(default=datetime.datetime.now)
    emissions_per_kg = FloatField(null=False)
    ingredients = TextField(null=False)
EmissionsList.create_table()
