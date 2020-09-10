from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField
from wtforms.validators import InputRequired, Optional, NumberRange, URL

class PetForm(FlaskForm):

    name = StringField("Pet Name")
    species = SelectField("Species", choices=[('cat','Cat'), ('dog', 'Dog'), ('porc', 'Porcupine')])
    image_url = StringField("Photo URL", validators=[URL(require_tld=True, message="Please enter a url."), Optional()])
    age = FloatField("Age", validators=[NumberRange(min=0, max=30, message="Please enter a valid age.")])
    notes = StringField("Notes")