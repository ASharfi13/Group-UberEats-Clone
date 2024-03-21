from flask import Blueprint, request
from flask_login import login_required
from app.models import User, db
from app.utils import get_current_user
import json

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
@login_required
def users():
    """
    Query for all users and returns them in a list of user dictionaries
    """
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
@login_required
def user(id):
    """
    Query for a user by id and returns that user in a dictionary
    """
    user = User.query.get(id)
    return user.to_dict()


@user_routes.route('/<int:id>/add-funds', methods =['PUT'])
@login_required
def wallet(id):
    incoming_funds = float(json.loads(request.data)['funds'])
    user = User.query.get(id)
    user.wallet += incoming_funds
    db.session.commit()
    return str(user.wallet)

@user_routes.route('/<int:id>/get-funds')
@login_required
def get_wallet(id):
    user = User.query.get(id)
    return str(user.wallet)
