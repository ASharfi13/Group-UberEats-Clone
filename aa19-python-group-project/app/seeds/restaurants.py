from app.models import db, Restaurant, SCHEMA, environment
from sqlalchemy.sql import text

def seed_restaurants():
    restaurant1 = Restaurant(
        name="Burger King", location="123 Ave", type="Fast Food", owner_id="1", imageUrl="https://cdn.freebiesupply.com/images/large/2x/burger-king-logo-png-transparent.png"
    )

    db.session.add(restaurant1)
    db.session.commit()


def undo_restaurants():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.restaurants RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM restaurants"))

    db.session.commit()
