from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class RestaurantForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()])
    type = StringField('type', validators=[DataRequired()])
    imageUrl = StringField('imageUrl', validators=[DataRequired()])
