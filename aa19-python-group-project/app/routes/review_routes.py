from flask import Blueprint, Flask, request, Response
from app.models import db, Review
import json

review_routes = Blueprint("reviews", __name__)

# CREATE A REVIEW FOR A RESTAURANT BASED ON ID/Still need error handling
@review_routes.route('restaurants/<int:restaurantId>/reviews', methods=["POST"])
def createReview(restaurantId):
    data = request.json
    newReview = Review(**data, restaurant_id=restaurantId)
    db.session.add(newReview)
    db.session.commit()
    responseObj = {
        "id": newReview.id,
        "userId": newReview.user_id,
        "restaurantId": newReview.restaurant_id,
        "description": newReview.description,
        "stars": newReview.stars,
        "createdAt": newReview.createdAt
    }
    return Response(json.dumps(responseObj), status=201)

@review_routes.route('restaurants/<int:restaurantId>/reviews', methods=["GET"])
def getReviews(restaurant_id):
    reviews = Review.query.get(id=reviewId).all()
    reviewResponse = [review.to_dict for review in reviews]
    return json.dumps(reviewResponse)


@review_routes.route('reviews/<int:reviewId>', methods=["DELETE"])
def deleteReview(reviewId):
    review = Review.query.get(id=reviewId)
    db.session.delete(review)
    db.session.commit()
    return json.dumps({
        "message": "Successfully deleted"
    })
