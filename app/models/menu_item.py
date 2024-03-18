from .db import db, SCHEMA, environment, add_prefix_for_prod
from sqlalchemy.orm import validates
from sqlalchemy import CheckConstraint
import re
import datetime as dt

class MenuItem(db.Model):
    __tablename__ = "menu_items"
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("restaurants.id")), nullable=False)
    imageUrl = db.Column(db.String, nullable=False)
    createdAt = db.Column(db.Date, default=dt.datetime.now())
    updatedAt = db.Column(db.Date, default=dt.datetime.now())

    restaurant = db.relationship("Restaurant", back_populates="menu_items")

    # @validates("name")
    # def validate_name(self):
    #     specialChars = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    #     if (specialChars.search(self.name) != None):
    #         raise ValueError("Name must only have alpha-numeric characters")
    #     return self.name

    # @validates("price")
    # def validate_price(self):
    #     if self.price < 0:
    #         raise ValueError("Price must be a positive number")
    #     return self.price

    # @validates("type")
    # def validate_type(self):
    #     if self.type not in []:
    #         raise ValueError("Invalid Type")
    #     return self.price

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'type': self.type,
            'imageUrl': self.imageUrl,
            'restaurant_id': self.restaurant_id,
        }
