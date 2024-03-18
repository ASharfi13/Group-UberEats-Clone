from .db import db, SCHEMA, add_prefix_for_prod, environment
from sqlalchemy.orm import validates
from sqlalchemy import CheckConstraint
import re
import datetime as dt

class Restaurant(db.Model):
    __tablename__ = "restaurants"
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    imageUrl = db.Column(db.String)
    createdAt = db.Column(db.Date, default=dt.datetime.now())
    updatedAt = db.Column(db.Date, default=dt.datetime.now())

    reviews = db.relationship("Review", back_populates="restaurant", cascade='all, delete-orphan')
    menu_items = db.relationship("MenuItem", back_populates="restaurant", cascade='all, delete-orphan')

    # @validates("name")
    # def validate_name(self):
    #     specialChars = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    #     if (specialChars.search(self.name) != None):
    #         raise ValueError("Name must only have alpha-numeric characters")
    #     return self.name

    # @validates("type")
    # def validate_type(self):
    #     if self.type not in []:
    #         raise ValueError("Invalid Type")
    #     return self.price

    def to_dict(self):
        return {
            'id': self.id,
            "name": self.name,
            'owner_id': self.owner_id,
            'location': self.location,
            'type': self.type,
            'reviews': [review.to_dict() for review in self.reviews],
            'imageUrl': self.imageUrl
        }
