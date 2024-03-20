from flask import Blueprint, Flask, request
from app.models import db, Review
from flask_login import login_required
from app.utils import is_review_owner, get_current_user
import json

review_routes = Blueprint("reviews", __name__)

# DELETE A REVIEW
@review_routes.route('/<int:reviewId>', methods=["DELETE"])
@login_required
@is_review_owner
def deleteReview(reviewId):
    review = Review.query.get(reviewId)

    if not review:
        return json.dumps({
            "message": "Review couldn't be found"
        }), 404

    db.session.delete(review)
    db.session.commit()
    return json.dumps({
        "message": "Successfully deleted"
    })

@review_routes.route("/current")
@login_required
def getAllReviewByCurrentOwner():
    reviews = Review.query.filter_by(user_id=get_current_user()).all()
    return json.dumps([review.to_dict() for review in reviews])
