from flask import Blueprint, Flask, request
# from app.posts import users, posts
from app.models import db, MenuItem
import json

menu_item_routes = Blueprint("menu-items", __name__)

# get details of a menu_item from an id
# /<int:itemId>
@menu_item_routes.route('/<int:itemId>')
def getAllDetails(itemId):
    menu_item_detail= MenuItem.query.get(itemId)
    return json.dumps(menu_item_detail.to_dict())

# create a menu item
#/restaurants/<int:restaurantId>/menu-items
# # this might have to go IN THE RESTAURANTS ROUTES
# @menu_item_routes.route("/restaurant/<int:itemId>/menu-items", methods=["POST"])
# def createMenuItem(itemId):
#     data = request.json
#     newItem = MenuItem(**data, restaurant_id=itemId)
#     db.session.add(newItem)
#     db.session.commit()
#     return json.dumps(newItem.to_dict())


# edit a menu item
# /<int:itemId>
@menu_item_routes.route("/<int:itemId>", methods=["PUT"])
def updateMenuItem(itemId):
    item = MenuItem.query.get(itemId)
    newData = request.json

    badReq = {
        "message": "Bad Request",
        "errors":{}
    }
    errCount = 0
    if len(newData["name"]) == 0:
        badReq["errors"]["name"] = "Name is required"
        errCount += 1
    if len(newData["price"]) == 0:
        badReq["errors"]["price"] = "Price is required"
        errCount += 1
    if len(str(newData["type"])) == 0:
        badReq["errors"]["type"] = "Type is required"
        errCount += 1
    if len(newData["imageUrl"]) == 0:
        badReq["errors"]["imageUrl"] = "Image Url is required"
        errCount += 1

    if errCount > 0:
        return json.dumps(badReq), 400

    for keys in newData:
        setattr(item, keys, newData.get(keys))

    db.session.commit()
    return json.dumps(item.to_dict())



# delete a menu item
# /<int:itemId>
@menu_item_routes.route("/<int:itemId>", methods=["DELETE"])
def deleteMenuItem(itemId):
    item = MenuItem.query.get(itemId)

    if item == None:
        return json.dumps({
            "message": "Menu Item couldn't be found"
        })

    db.session.delete(item)
    db.session.commit()
    return json.dumps({
        "message": "Successfully Deleted",
        "id": itemId
    })