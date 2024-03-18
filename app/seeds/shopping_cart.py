from app.models import db, ShoppingCart, SCHEMA, environment
from sqlalchemy.sql import text

def seed_shopping_cart():
    cart1 = ShoppingCart(
        user_id=1, menu_item_id=1
    )
    db.session.add(cart1)
    db.session.commit()

def undo_shopping_cart():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.shopping_carts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM shopping_carts"))

    db.session.commit()
