from flask_wtf import FlaskForm
from wtforms import StringField, FloatField

class PetForm(FlaskForm):

    name = StringField("Pet Name")
    species = StringField("Species")
    image_url = StringField("Photo URL")
    age = FloatField("Age")
    notes = StringField("Notes")