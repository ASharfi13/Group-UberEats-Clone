from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import DataRequired, NumberRange, ValidationError

def two_decimals(form, field):
    dec = str(field.data).split(".")[1]
    if dec and len(dec) > 2:
        raise ValidationError('Price must have 2 decimals or less')

class MenuItemForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    price = FloatField('price', validators=[DataRequired(), NumberRange(min=0), two_decimals])
    type = StringField('type', validators=[DataRequired()])
    imageUrl = StringField('imageUrl', validators=[DataRequired()])
