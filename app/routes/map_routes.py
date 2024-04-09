from flask import Blueprint, request
from app.config import Config
from app.models import db
from flask_login import login_required

map_routes = Blueprint('maps', __name__)


@map_routes.route('/key', methods=["POST"])
@login_required
def getKey():
    """
    Returns Google Maps API key to Front-end
    """
    return {"key": Config.GOOGLE_MAPS_API}, 200
