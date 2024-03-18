from app.models import db, Review, environment, SCHEMA
from sqlalchemy.sql import text
from .seed_data import reviews

def seed_reviews():
    review1 = Review(
        stars=3, description="It wasn't all that", user_id=1, restaurant_id=1
    )
    db.session.add(review1)
    db.session.commit()


def undo_reviews():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))

    db.session.commit()
