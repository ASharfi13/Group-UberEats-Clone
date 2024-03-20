from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange

class ReviewForm(FlaskForm):
    description = StringField('description', validators=[DataRequired("Description is required")])
    stars = IntegerField('stars', validators=[DataRequired("Stars are required"), NumberRange(min=1, max=5)])
