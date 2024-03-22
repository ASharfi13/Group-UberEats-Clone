from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import DataRequired, NumberRange, ValidationError
from app.models.menu_item import menuItemTypes
import re

def two_decimals(form, field):
    check = str(field.data).split(".")
    if len(check) > 1:
        dec=check[1]
        if dec and len(dec) > 2:
            raise ValidationError('Price must have 2 decimals or less')

def valid_type(form, field):
    if field.data not in menuItemTypes:
        raise ValidationError("Invalid Type")

def no_special_char(form, field):
    specialChars = re.compile('[@_!$%^&*()<>?/\|}{~:]')
    if (specialChars.search(field.data) != None):
        raise ValidationError(f"{field.name.capitalize()} must not contain special characters")

class MenuItemForm(FlaskForm):
    name = StringField('name', validators=[DataRequired("Name is required"), no_special_char])
    price = FloatField('price', validators=[DataRequired("Price is required"), NumberRange(min=0), two_decimals])
    type = StringField('type', validators=[DataRequired("Type is required"), valid_type])
    imageUrl = StringField('imageUrl', validators=[DataRequired("Image is required")])
