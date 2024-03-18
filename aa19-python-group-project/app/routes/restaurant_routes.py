from app.models import db, Restaurant, MenuItem
from flask import Blueprint, request
import json



restaurant_routes = Blueprint("restaurants", __name__)

#GET ALL RESTAURANTS at ["/api/restaurants"]
@restaurant_routes.route("/")
def allRestaurants():
    restaurants = Restaurant.query.all()
    return json.dumps({"restaurants":[restaurant.to_dict() for restaurant in restaurants]})

#CREATE A NEW RESTAURANT at ["/api/restaurants"]
@restaurant_routes.route("/", methods=["POST"])
def newRestaurant():
    data = request.json
    badReq = {
        "message": "Bad Request",
        "errors":{}
    }
    errCount = 0
    if len(data["name"]) == 0:
        badReq["errors"]["name"] = "Name is required"
        errCount += 1
    if len(data["location"]) == 0:
        badReq["errors"]["location"] = "Location is required"
        errCount += 1
    if len(str(data["type"])) == 0:
        badReq["errors"]["type"] = "Type is required"
        errCount += 1
    if data["owner_id"] == None:
        badReq["errors"]["owner_id"] = "Owner Id is required"
        errCount += 1
    if len(data["imageUrl"]) == 0:
        badReq["errors"]["imageUrl"] = "Image Url is required"
        errCount += 1

    if errCount > 0:
        return json.dumps(badReq), 400

    newRestaurant = Restaurant(**data)
    db.session.add(newRestaurant)
    db.session.commit()
    return json.dumps(newRestaurant.to_dict())

#GET ALL RESTAURANTS BY CURRENT USER at ["/api/restaurants/current"]
@restaurant_routes.route("/current/<int:id>")
def allCurrentUserRestaurants(id):
    #ID HAS BEEN IMPLEMENTED TO TEST FUNCTIONALITY, PLEASE REFACTOR IN THE FUTURE WHEH FRONTEND URL IS ESTABLISHED
    #***ID HERE REPRESENTS USER ID, NOT RESTAURANT ID***
    allUserRestaurants = Restaurant.query.filter_by(owner_id=id).all()
    return json.dumps({"restaurants": [restaurant.to_dict() for restaurant in allUserRestaurants]})

#GET RESTAURANT DETAILS BY ID
@restaurant_routes.route("/<int:id>")
def getRestaurantById(id):
    restaurant = Restaurant.query.get(id)
    # restaurant_form["Reviews"] = [review.to_dict() for review in restaurant.reviews]
    if restaurant == None:
        return json.dumps({
            "message": "Restaurant couldn't be found"
        }), 404

    reviews = [review.to_dict() for review in restaurant.reviews]
    totalStarRating = 0
    for review in reviews:
        del review["restaurant"]
        totalStarRating += review["stars"]

    if len(reviews) != 0:
        avgRating = totalStarRating / len(reviews)
    else:
        avgRating = 0
    restaurant_formatted = {
        "id": restaurant.id,
        "owner_id": restaurant.owner_id,
        "location": restaurant.location,
        "name": restaurant.name,
        "type": restaurant.type,
        "avgRating": avgRating,
        "numReviews": len(reviews),
        "Reviews": reviews,
        "MenuItems": [menu_item.to_dict() for menu_item in restaurant.menu_items]
    }
    print(reviews)
    return json.dumps(restaurant_formatted)

#EDIT/UPDATE A RESTAURANT at ["/api/restaurant/id"]
@restaurant_routes.route("/<int:id>", methods=["PUT"])
def updateRestaurant(id):
    restaurant = Restaurant.query.get(id)

    if restaurant == None:
        return json.dumps({
            "message": "Restaurant couldn't be found"
        }), 404

    data = request.json
    badReq = {
        "message": "Bad Request",
        "errors":{}
    }
    errCount = 0
    if len(data["name"]) == 0:
        badReq["errors"]["name"] = "Name is required"
        errCount += 1
    if len(data["location"]) == 0:
        badReq["errors"]["location"] = "Location is required"
        errCount += 1
    if len(str(data["type"])) == 0:
        badReq["errors"]["type"] = "Type is required"
        errCount += 1
    if len(data["imageUrl"]) == 0:
        badReq["errors"]["imageUrl"] = "Image Url is required"
        errCount += 1

    if errCount > 0:
        return json.dumps(badReq), 400

    for keys in data:
        setattr(restaurant, keys, data.get(keys))

    db.session.commit()
    return json.dumps(restaurant.to_dict())

#DELETE A RESTAURANT at ["/api/restaurants/id"]
@restaurant_routes.route("/<int:id>", methods=["DELETE"])
def deleteRestaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant == None:
        return json.dumps({
            "message": "Restaurant couldn't be found"
        })

    db.session.delete(restaurant)
    db.session.commit()
    return json.dumps({
        "message": "Successfully deleted"
    })

# create a menu item
#/restaurants/<int:restaurantId>/menu-items
# this might have to go IN THE RESTAURANTS ROUTES
@restaurant_routes.route("/<int:restaurantId>/menu-items", methods=["POST"])
def createMenuItem(restaurantId):
    data = request.json
    badReq = {
        "message": "Bad Request"
    }
    newItem = MenuItem(**data, restaurant_id=restaurantId)
    db.session.add(newItem)
    db.session.commit()
    return json.dumps(newItem.to_dict())
