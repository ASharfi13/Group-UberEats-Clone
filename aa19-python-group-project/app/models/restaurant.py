from .db import db, SCHEMA, add_prefix_for_prod, environment
from sqlalchemy.orm import validates
from sqlalchemy import CheckConstraint
from .seed_data import restaurants
import datetime as dt

class Restaurant(db.Model):
    __tablename__ = "restaurants"
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

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

    def to_dict(self):
        return {
            'id': self.id,
            'owner_id': self.owner_id,
            'location': self.location,
            'type': self.type,
            'imageUrl': self.imageUrl
        }
