from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class inputForm(FlaskForm):
    lstNames = SelectField("Student First Name")
    Search = SubmitField('Search')