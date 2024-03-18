from app.models import db, Review, environment, SCHEMA
from sqlalchemy.sql import text
from .seed_data import reviews

def seed_reviews():
    for review in reviews:
<<<<<<< HEAD
        newRes = Review(**review)
        db.session.add(newRes)
=======
        newReview = Review(**review)
        db.session.add(newReview)
>>>>>>> 5d4fbf9f0bf0baaf27ebd5d3a064b9170ef54ccb
    db.session.commit()



def undo_reviews():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))

    db.session.commit()
