from flask.cli import AppGroup
from .users import seed_users, undo_users
from .restaurants import seed_restaurants, undo_restaurants
from .reviews import seed_reviews, undo_reviews
from .menu_item import seed_menu_items, undo_menu_items
from .shopping_cart import seed_shopping_cart, undo_shopping_cart

from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_users()
        undo_restaurants()
        undo_menu_items()
        undo_reviews()
        undo_shopping_cart()
    seed_users()
    seed_restaurants()
    seed_menu_items()
    seed_reviews()
    seed_shopping_cart()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_restaurants()
    undo_menu_items()
    undo_reviews()
    undo_shopping_cart()
    # Add other undo functions here
