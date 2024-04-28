from app.models import db, RestaurantType, SCHEMA, environment, Restaurant
from sqlalchemy.sql import text
from .seed_data import restaurant_types, restaurant_type_associations

def seed_types():
    for restaurant_type in restaurant_types:
        newRes = RestaurantType(**restaurant_type)
        db.session.add(newRes)
    db.session.commit()


def undo_types():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.restaurant_types RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM restaurant_types"))

    db.session.commit()

def seed_associations():
    for association in restaurant_type_associations:
        restaurant = Restaurant.query.get(association["restaurant_id"])
        rType = RestaurantType.query.get(association["type_id"])
        # newAss = RestaurantTypeAssociation(**association)
        restaurant.types.append(rType)
    db.session.commit()

def undo_associations():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.restaurant_type_associations RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM restaurant_type_associations"))

    db.session.commit()
