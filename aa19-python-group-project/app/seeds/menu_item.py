from app.models import db, MenuItem, SCHEMA, environment
from sqlalchemy.sql import text

def seed_menu_items():
    menu_item1 = MenuItem(
        name="Hamburger", type="Burger", price=10.99, restaurant_id=1, imageUrl="https://cdn.freebiesupply.com/images/large/2x/burger-king-logo-png-transparent.png"
    )
    db.session.add(menu_item1)
    db.session.commit()

def undo_menu_items():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.menu_items RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM menu_items"))

    db.session.commit()
