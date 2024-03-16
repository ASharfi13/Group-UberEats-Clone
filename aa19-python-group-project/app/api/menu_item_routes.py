from flask import Blueprint, Flask, request
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
@menu_item_routes.route("/restaurant/<int:id>/menu-items", methods=["POST"])
def createMenuItem(id):
    data = request.json
    newItem = MenuItem(**data, restaurant_id=id)
    db.session.add(newItem)
    db.session.commit()
    return json.dumps(newItem.toDict())


# edit a menu item
# /<int:itemId>
@menu_item_routes.route("/<int:id>", methods=["PUT"])
def updateMenuItem(id):
    item = MenuItem.query.get(id)
    newData = request.json
    for keys in newData:
        setattr(item, keys, newData.get(keys))
    db.session.commit()
    return json.dumps(item.toDict())



# delete a menu item
# /<int:itemId>
@app.route("/<int:id>", methods=["DELETE"])
def deleteMenuItem(id):
    item = MenuItem.query.get(id)
    db.session.delete(item)
    db.session.commit()
    return json.dumps({
        "id": id
    })
