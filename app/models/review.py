from .db import db, SCHEMA, environment, add_prefix_for_prod
from sqlalchemy.orm import validates
from sqlalchemy import CheckConstraint
import datetime as dt

class Review(db.Model):
    __tablename__ = "reviews"
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id=db.Column(db.Integer, primary_key=True)
    stars=db.Column(db.Integer, nullable=False)
    description=db.Column(db.Text, nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey("users.id"))
    restaurant_id=db.Column(db.Integer, db.ForeignKey("restaurants.id", ondelete="CASCADE"))
    createdAt = db.Column(db.Date, default=dt.datetime.now())
    updatedAt = db.Column(db.Date, default=dt.datetime.now())
    restaurant = db.relationship("Restaurant", back_populates = "reviews")

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'stars': self.stars,
            'description': self.description,
            'restaurant': self.restaurant.to_dict()
        }
