from flask import Blueprint, Flask, request
from app.models import db, MenuItem
from app.models.menu_item import menuItemTypes
from app.forms import MenuItemForm
from flask_login import login_required
from app.utils import is_menu_item_owner
import json
from types import SimpleNamespace

menu_item_routes = Blueprint("menu-items", __name__)

# GET DETAILS FOR MENU ITEM BY ID at ["/api/menu-items/:itemId"]
@menu_item_routes.route('/<int:itemId>')
def getAllDetails(itemId):
    item = MenuItem.query.get(itemId)
    if not item:
        return json.dumps({
            "message": "Menu Item couldn't be found"
        }), 404
    return json.dumps(item.to_dict())

# GET ALL menu-item TYPES at ["/api/menu-items/types"]
@menu_item_routes.route("/types")
def allMenuItemTypes():
    return json.dumps(menuItemTypes)

# EDIT A MENU ITEM BY ID at ["/api/menu-items/:itemId"]
@menu_item_routes.route("/<int:itemId>", methods=["PUT"])
@login_required
@is_menu_item_owner
def updateMenuItem(itemId):
    item = MenuItem.query.get(itemId)

    if not item:
        return json.dumps({
            "message": "Menu Item couldn't be found"
        }), 404

    data = json.loads(request.data, object_hook=lambda d: SimpleNamespace(**d)) # convert JSON to Object so form can key in using .
    form = MenuItemForm(obj=data)
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        form.populate_obj(item)
        db.session.add(item)
        db.session.commit()
        return json.dumps(item.to_dict())
    return {'message': 'Bad Request', 'errors': form.errors}, 400



# DELETE A MENU ITEM BY ID at ["/api/menu-items/:itemId"]
@menu_item_routes.route("/<int:itemId>", methods=["DELETE"])
@login_required
@is_menu_item_owner
def deleteMenuItem(itemId):
    item = MenuItem.query.get(itemId)

    if not item:
        return json.dumps({
            "message": "Menu Item couldn't be found"
        }), 404

    db.session.delete(item)
    db.session.commit()
    return json.dumps({
        "message": "Successfully deleted"
    })
