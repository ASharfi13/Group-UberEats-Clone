from app.models import db, Restaurant, SCHEMA, environment
from sqlalchemy.sql import text
from .seed_data import restaurants

def seed_restaurants():
    for restaurant in restaurants:
        newRes = Restaurant(**restaurant)
        db.session.add(newRes)
    db.session.commit()


def undo_restaurants():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.restaurants RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM restaurants"))

    db.session.commit()

