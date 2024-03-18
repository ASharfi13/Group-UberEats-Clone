from .db import db, SCHEMA, environment, add_prefix_for_prod
from sqlalchemy.orm import validates
from sqlalchemy import CheckConstraint
import datetime as dt

class ShoppingCart(db.Model):
    __tablename__ = "shopping_carts"
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id= db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    menu_item_id=db.Column(db.Integer, db.ForeignKey("menu_items.id"))
    checkedOut= db.Column(db.Boolean, default=False)
    order_id=db.Column(db.Integer, default=1)
    createdAt = db.Column(db.Date, default=dt.datetime.now())
    updatedAt = db.Column(db.Date, default=dt.datetime.now())

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'menu_item_id': self.menu_item_id,
            'order_id': self.order_id
        }
