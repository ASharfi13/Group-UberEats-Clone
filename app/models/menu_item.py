from .db import db, SCHEMA, environment, add_prefix_for_prod
import datetime as dt

menuItemTypes = [
    "Appetizer",
    "Entree",
    "Dessert",
    "Drink",
    "Salad",
    "Soup",
    "Burger",
    "Pizza",
    "Chicken",
    "Taco",
    "Beef",
    "Rice",
    "Pork",
    "Shrimp",
    "Burrito",
    "Noodle",
    "Ice Cream",
    "Cake",
    "Pie"
]

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

    shopping_carts = db.relationship("ShoppingCart", back_populates="menu_item", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'type': self.type,
            'imageUrl': self.imageUrl,
            'restaurant_id': self.restaurant_id,
        }
