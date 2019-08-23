from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField
from wtforms.validators import InputRequired


class AddPetForm(FlaskForm):
    "Form for adding a Pet "

    name = StringField('Pet Name', validators=[InputRequired()])

    species = StringField('Species')

    photo_url = StringField('Photo Url')

    age = FloatField('Age')

    notes = StringField('Notes')
