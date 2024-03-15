from .db import db
from sqlalchemy.orm import validates
from sqlalchemy import CheckConstraint
import datetime as dt

class Review(db.Model):
    __tablename__ = "reviews"
    __table_args__ = ()

    id=db.Column(db.Integer, primary_key=True)
    stars=db.Column(db.Integer, nullable=False)
    description=db.Column(db.Text, nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey("users.id"))
    restaurant_id=db.Column(db.Integer, db.ForeignKey("restaurants.id", ondelete="CASCADE"))
    createdAt = db.Column(db.Date, default=dt.datetime.now())
    updatedAt = db.Column(db.Date, defailt=dt.datetime.now())
