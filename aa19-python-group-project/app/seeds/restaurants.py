from app.models import db, Restaurant, SCHEMA, environment
from sqlalchemy.sql import text

def seed_restaurants():
    restaurant1 = Restaurant(
        name="Burger King", location="123 Ave", type="Fast Food", owner_id="1", imageUrl="https://cdn.freebiesupply.com/images/large/2x/burger-king-logo-png-transparent.png"
    )
