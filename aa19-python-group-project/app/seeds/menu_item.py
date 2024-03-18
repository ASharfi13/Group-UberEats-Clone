from app.models import db, MenuItem, SCHEMA, environment
from sqlalchemy.sql import text
from .seed_data import menu_items

def seed_menu_items():
    for menu_item in menu_items:
        newRes = MenuItem(**menu_item)
        db.session.add(newRes)
    db.session.commit()

def undo_menu_items():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.menu_items RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM menu_items"))

    db.session.commit()
