from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange

class ReviewForm(FlaskForm):
    description = StringField('description', validators=[DataRequired()])
    stars = IntegerField('stars', validators=[DataRequired(), NumberRange(min=1, max=5)])
