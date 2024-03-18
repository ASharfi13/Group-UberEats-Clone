from flask import Blueprint, Flask, request
from app.models import db, Review
import json

review_routes = Blueprint("reviews", __name__)

# CREATE A REVIEW FOR A RESTAURANT BASED ON ID/Still need error handling
@review_routes.route('/restaurants/<int:restaurantId>/reviews', methods=["POST"])
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
        "createdAt": str(newReview.createdAt)
    }
    return json.dumps(responseObj), 201


# GET REVIEWS
@review_routes.route('/restaurants/<int:restaurantId>/reviews', methods=["GET"])
def getReviews(restaurantId):
    reviews = Review.query.filter_by(restaurant_id=restaurantId).all()
    reviewResponse = [review.to_dict() for review in reviews]

    return json.dumps(reviewResponse)

# DELETE A REVIEW
@review_routes.route('/reviews/<int:reviewId>', methods=["DELETE"])
def deleteReview(reviewId):
    review = Review.query.get(reviewId)
    db.session.delete(review)
    db.session.commit()
    return json.dumps({
        "message": "Successfully deleted"
    })
