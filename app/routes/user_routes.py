from flask import Blueprint, request
from flask_login import login_required
from app.models import User, db
from app.utils import get_current_user

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


@user_routes.route('/add-funds', methods =['PUT'])
@login_required
def wallet():

    incoming_funds = request.data['funds']
    user = User.query.get(get_current_user())
    user.wallet += incoming_funds
    db.session.commit()
    return user.to_dict_private()

@user_routes.route('/get-funds')
@login_required
def get_wallet():

    user = User.query.get(get_current_user())
    return user.wallet
