from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError
from app.models.restaurant import restaurantTypes
import re

def valid_type(form, field):
    if field.data not in restaurantTypes:
        raise ValidationError("Invalid Type")

def no_special_char(form, field):
    specialChars = re.compile('[@_!$%^&*()<>?/\|}{~:]')
    if (specialChars.search(field.data) != None):
        raise ValidationError(f"{field.name.capitalize()} must not contain special characters")

class RestaurantForm(FlaskForm):
    name = StringField('name', validators=[DataRequired("Name is required"), no_special_char])
    location = StringField('location', validators=[DataRequired("Location is required"), no_special_char])
    type = StringField('type', validators=[DataRequired("Type is required"), valid_type])
    imageUrl = StringField('imageUrl', validators=[DataRequired("Image is required")])
