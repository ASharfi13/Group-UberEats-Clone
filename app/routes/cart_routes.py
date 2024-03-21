from app.models import db, MenuItem, User, ShoppingCart
from flask import Blueprint, request
from flask_login import login_required
from app.utils import get_current_user
import json

cart_routes = Blueprint("shopping-carts", __name__)

# GET ALL ORDERS at [/api/shopping-carts/:user_id]
@cart_routes.route("/<int:user_id>")
@login_required
def allOrders(user_id):
    orderItems = ShoppingCart.query.filter_by(user_id=user_id).all()
    allMenuItems = MenuItem.query.all()
    menuItemDict = {item.id : item for item in allMenuItems}

    orders = {}
    for item in orderItems:
        # menu_item = MenuItem.query.get(item.menu_item_id)
        try:
            if item.order_id not in orders:
                orders[item.order_id] = {
                    "order_id": item.order_id,
                    "restaurant": menuItemDict.get(item.menu_item_id).restaurant.name,
                    "items" : [menuItemDict.get(item.menu_item_id).to_dict()],
                    "createdAt": str(item.createdAt)
            }
            else:
                orders[item.order_id]['items'].append(menuItemDict.get(item.menu_item_id).to_dict())
        except:
            continue


    return json.dumps({"orders": list(orders.values())})

# CHECKOUT CURRENT CART at ["/api/shopping-carts/check-out"]
@cart_routes.route("/check-out", methods=["POST"])
@login_required # add sufficient balance check
def checkoutCart():
    payload = json.loads(request.data)
    user = User.query.get(payload["user_id"])
    orderId = user.order_id
    for item in payload["cart_items"]:
        item = json.loads(item)
        print(item)
        newCartItem = ShoppingCart(
            user_id = payload["user_id"],
            menu_item_id = item["id"],
            order_id = orderId
        )
        db.session.add(newCartItem)
    db.session.commit()
    response = {
        "order_id": orderId,
        "restaurant": item["restaurant"],
        "items": payload["cart_items"],
        "createdAt": str(newCartItem.createdAt)
    }
    user.order_id += 1
    db.session.add(user)
    db.session.commit()
    return json.dumps(response), 201



# [
#     {
#         user_id: 1,
#         order_id: 1,
#         menu_item_id: 1,
#         createdAt: "June 18, 2025"
#     },
#     ...
# ]
# {
#   "orders": [
#     {
#       "order_id": 1,
#       "items": [
#           1,
#           7,
#           8
#       ],
#       "createdAt": "June 18, 2024"
#     }
#   ]
# }
