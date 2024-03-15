from .db import db, SCHEMA
from sqlalchemy.orm import validates
from sqlalchemy import CheckConstraint
import datetime as dt

class Restaurant(db.Model):
    __tablename__ = "restaurants"
    __table_args__= (
        {'schema': SCHEMA}
    )

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False, unique=True )
    type = db.Column(db.String, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    imageUrl = db.Column(db.String)
    createdAt = db.Column(db.Date, default=dt.datetime.now())
    updatedAt = db.Column(db.Date, default=dt.datetime.now())

    reviews = db.relationship("Review", back_populates="restaurant", cascade='all, delete-orphan')
    menu_items = db.relationship("MenuItem", back_populates="restaurant", cascade='all, delete-orphan')
