from .db import db, SCHEMA
from sqlalchemy.orm import validates
from sqlalchemy import CheckConstraint
import datetime as dt

class MenuItem(db.Model):
    __tablename__ = "menu_items"
    __table_args__ = (
        {'schema': SCHEMA}
    )

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.id"), nullable=False)
    imageUrl = db.Column(db.String, nullable=False)
    createdAt = db.Column(db.Date, default=dt.datetime.now())
    updatedAt = db.Column(db.Date, default=dt.datetime.now())

    restaurant = db.relationship("Restaurant", back_populates="menu_items")
