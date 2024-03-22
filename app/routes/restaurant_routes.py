from app.models import db, Restaurant, MenuItem, Review, User
from app.models.restaurant import restaurantTypes
from app.forms import RestaurantForm, MenuItemForm, ReviewForm
from flask import Blueprint, request
from flask_login import login_required
from app.utils import is_restaurant_owner, get_current_user
import json
from types import SimpleNamespace

restaurant_routes = Blueprint("restaurants", __name__)

#GET ALL RESTAURANTS at ["/api/restaurants"]
@restaurant_routes.route("/")
def allRestaurants():
    restaurants = Restaurant.query.all()
    return json.dumps({"restaurants":[restaurant.to_dict() for restaurant in restaurants]})

#GET ALL RESTAURANT TYPES at ["/api/restaurants/types"]
@restaurant_routes.route("/types")
def allRestaurantTypes():
    return json.dumps(restaurantTypes)

#CREATE A NEW RESTAURANT at ["/api/restaurants"]
@restaurant_routes.route("/", methods=["POST"])
@login_required
def newRestaurant():
    form = RestaurantForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        newRestaurant = Restaurant(
            name=form.data['name'],
            location=form.data['location'],
            type=form.data['type'],
            imageUrl=form.data['imageUrl'],
            owner_id=get_current_user()
        )
        db.session.add(newRestaurant)
        db.session.commit()
        return json.dumps(newRestaurant.to_dict()), 201
    return {'message': 'Bad Request', 'errors': form.errors}, 400

#GET ALL RESTAURANTS BY CURRENT USER at ["/api/restaurants/current"]
@restaurant_routes.route("/current")
@login_required
def allCurrentUserRestaurants():
    id = get_current_user()
    allUserRestaurants = Restaurant.query.filter_by(owner_id=id).all()
    return json.dumps({"restaurants": [restaurant.to_dict() for restaurant in allUserRestaurants]})

#GET RESTAURANT DETAILS BY ID at ["/api/restaurant/:id"]
@restaurant_routes.route("/<int:id>")
def getRestaurantById(id):
    restaurant = Restaurant.query.get(id)
    # restaurant_form["Reviews"] = [review.to_dict() for review in restaurant.reviews]
    if not restaurant:
        return json.dumps({
            "message": "Restaurant couldn't be found"
        }), 404

    reviews = [review.to_dict() for review in restaurant.reviews]
    totalStarRating = 0
    for review in reviews:
        totalStarRating += review["stars"]
        review["name"]= User.query.filter_by(id = review['user_id'] ).first().name
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
        "MenuItems": [menu_item.to_dict() for menu_item in restaurant.menu_items],
        "imageUrl": restaurant.imageUrl
    }
    return json.dumps(restaurant_formatted)

#EDIT/UPDATE A RESTAURANT at ["/api/restaurant/:id"]
@restaurant_routes.route("/<int:restaurantId>", methods=["PUT"])
@login_required
@is_restaurant_owner
def updateRestaurant(restaurantId):
    restaurant = Restaurant.query.get(restaurantId)

    if not restaurant:
        return json.dumps({
            "message": "Restaurant couldn't be found"
        }), 404
    data = json.loads(request.data, object_hook=lambda d: SimpleNamespace(**d)) # convert JSON to Object so form can key in using .
    form = RestaurantForm(obj=data)
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        form.populate_obj(restaurant)
        db.session.add(restaurant)
        db.session.commit()
        return json.dumps(restaurant.to_dict())
    return {'message': 'Bad Request', 'errors': form.errors}, 400

#DELETE A RESTAURANT at ["/api/restaurants/id"]
@restaurant_routes.route("/<int:restaurantId>", methods=["DELETE"])
@login_required
@is_restaurant_owner
def deleteRestaurant(restaurantId):
    restaurant = Restaurant.query.get(restaurantId)
    if not restaurant:
        return json.dumps({
            "message": "Restaurant couldn't be found"
        }), 404

    db.session.delete(restaurant)
    db.session.commit()
    return json.dumps({
        "message": "Successfully deleted"
    })

# GET ALL MENU ITEMS of RESTAURANT at ["/api/restaurants/id/menu-items"]
@restaurant_routes.route("/<int:restaurantId>/menu-items")
def getMenuItems(restaurantId):
    menuItems = MenuItem.query.filter_by(restaurant_id=restaurantId).all()
    return json.dumps({"items":[item.to_dict() for item in menuItems]})

# CREATE A MENU ITEM at ["/api/restaurants/id/menu-items"]
@restaurant_routes.route("/<int:restaurantId>/menu-items", methods=["POST"])
@login_required
@is_restaurant_owner
def createMenuItem(restaurantId):
    form = MenuItemForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        newItem = MenuItem(
            name=form.data['name'],
            price=form.data['price'],
            type=form.data['type'],
            imageUrl=form.data['imageUrl'],
            restaurant_id=restaurantId
        )
        db.session.add(newItem)
        db.session.commit()
        return json.dumps(newItem.to_dict()), 201
    return {'message': 'Bad Request', 'errors': form.errors}, 400

# CREATE A REVIEW FOR A RESTAURANT BASED ON ID
@restaurant_routes.route('/<int:restaurantId>/reviews', methods=["POST"])
@login_required
def createReview(restaurantId):
    restaurant = Restaurant.query.get(restaurantId)
    if not restaurant:
        return json.dumps({
            "message": "Restaurant couldn't be found"
        }), 404

    form = ReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        newReview = Review(
            description=form.data['description'],
            stars=form.data['stars'],
            user_id=get_current_user(),
            restaurant_id=restaurantId
        )
        db.session.add(newReview)
        db.session.commit()
        responseObj = {
            "id": newReview.id,
            "user_id": newReview.user_id,
            "restaurant_id": newReview.restaurant_id,
            "description": newReview.description,
            "stars": newReview.stars,
            "createdAt": str(newReview.createdAt)
        }
        return json.dumps(responseObj), 201
    return {'message': 'Bad Request', 'errors': form.errors}, 400

# GET REVIEWS
@restaurant_routes.route('/<int:restaurantId>/reviews', methods=["GET"])
def getReviews(restaurantId):
    reviews = Review.query.filter_by(restaurant_id=restaurantId).all()
    reviewResponse = [review.to_dict() for review in reviews]

    return json.dumps(reviewResponse)
