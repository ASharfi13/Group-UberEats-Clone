from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired, NumberRange, ValidationError
from app.models.menu_item import menuItemTypes
from app.utils.aws import ALLOWED_EXTENSIONS
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

def find_file_extension(filename):
    ext = ""
    for c in reversed(filename):
        if c != '.':
            ext = c + ext
        else:
            break

    return ext

def editImage(form, field):
    image = field.data
    if image == None:
        return True
    file_extension = find_file_extension(image.filename)
    if file_extension not in list(ALLOWED_EXTENSIONS):
        raise ValidationError('Allowed file types are .jpg, .jpeg, .png, .gif')

class MenuItemForm(FlaskForm):
    name = StringField('name', validators=[DataRequired("Name is required"), no_special_char])
    price = FloatField('price', validators=[DataRequired("Price is required"), NumberRange(min=0), two_decimals])
    type = StringField('type', validators=[DataRequired("Type is required"), valid_type])
    image = FileField('image_file', validators=[FileRequired("Image File is required"), FileAllowed(list(ALLOWED_EXTENSIONS))])

class EditMenuItemForm(FlaskForm):
    name = StringField('name', validators=[DataRequired("Name is required"), no_special_char])
    price = FloatField('price', validators=[DataRequired("Price is required"), NumberRange(min=0), two_decimals])
    type = StringField('type', validators=[DataRequired("Type is required"), valid_type])
    image = FileField("image_file", validators=[editImage])
