from flask_wtf import FlaskForm
from wtforms import StringField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired, ValidationError
from app.models.restaurant import restaurantTypes
from app.utils.aws import ALLOWED_EXTENSIONS
import re

def valid_type(form, field):
    if field.data not in restaurantTypes:
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

class RestaurantForm(FlaskForm):
    name = StringField('name', validators=[DataRequired("Name is required"), no_special_char])
    location = StringField('location', validators=[DataRequired("Location is required"), no_special_char])
    type = StringField('type', validators=[DataRequired("Type is required"), valid_type])
    image = FileField('image_file', validators=[FileRequired("Image File is Required"), FileAllowed(list(ALLOWED_EXTENSIONS))])

class EditRestaurantForm(FlaskForm):
    name = StringField('name', validators=[DataRequired("Name is required"), no_special_char])
    location = StringField('location', validators=[DataRequired("Location is required"), no_special_char])
    type = StringField('type', validators=[DataRequired("Type is required"), valid_type])
    image = FileField("image_file", validators=[editImage])
