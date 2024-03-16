from flask import Blueprint, render_template
# from app.posts import users, posts
from app.models import db, MenuItem
import json

menu_item_routes = Blueprint("menu-items", __name__)


# get details of a menu_item from an id
# /<int:itemId>
@menu_item_routes.route('/<int:itemId>')
def getAllDetails():
    menu_item_detail= MenuItem.query.get(id)
    return json.dumps(menu_item_detail.toDict())

# create a menu item
#/restaurants/<int:restaurantId>/menu-items
# this might have to go IN THE RESTAURANTS ROUTES

# edit a menu item
# /<int:itemId>

# delete a menu item
# /<int:itemId>
