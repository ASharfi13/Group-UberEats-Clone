from flask_login import current_user
from functools import wraps
from app.models import db, Restaurant, Review, MenuItem, ShoppingCart
import json

# Get current user
def get_current_user():
    if current_user.is_authenticated:
        return current_user.id
    return {'errors': {'message': 'Unauthorized'}}, 401

# Restaurant must belong to current user
def is_restaurant_owner(f):
    @wraps(f)
    def restaurant_authorization(restaurantId):
        userId = get_current_user()
        restaurant = Restaurant.query.get(restaurantId)
        if userId != restaurant.owner_id:
            return json.dumps({"message": "Forbidden"}), 403
        return f(restaurantId)
    return restaurant_authorization

# Menu Item must belong to current user
def is_menu_item_owner(f):
    @wraps(f)
    def menu_item_authorization(itemId):
        userId = get_current_user()
        menu_item = MenuItem.query.get(itemId)
        restaurant = Restaurant.query.get(menu_item.restaurant_id)
        if userId != restaurant.owner_id:
            return json.dumps({"message": "Forbidden"}), 403
        return f(itemId)
    return menu_item_authorization

# Review must belong to current user
def is_review_owner(f):
    @wraps(f)
    def review_authorization(reviewId):
        userId = get_current_user()
        review = Review.query.get(reviewId)
        if userId != review.user_id:
            return json.dumps({"message": "Forbidden"}), 403
        return f(reviewId)
    return review_authorization

# Cart must belong to current user
def is_cart_owner(f):
    @wraps(f)
    def cart_authorization(cartId):
        userId = get_current_user()
        cart = ShoppingCart.query.get(cartId)
        if userId != cart.user_id:
            return json.dumps({"message": "Forbidden"}), 403
        return f(id)
    return cart_authorization
