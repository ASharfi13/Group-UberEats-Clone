from .db import db, SCHEMA, add_prefix_for_prod, environment
import datetime as dt

restaurantTypes = [
    "American",
    "Chinese",
    "Indian",
    "Mexican",
    "Korean",
    "Thai",
    "Filipino",
    "Italian",
    "French",
    "Vietnamese",
    "Japanese",
    "Malaysian",
    "Peruvian",
    "Columbian",
    "German",
    "Russian",
    "Mediterranean",
    "Middle Eastern",
    "Hawaiian",
    "Other"
]
# class RestaurantTypeAssociation(db.Model):
#     __tablename__ = "restaurant_type_associations"
#     if environment == "production":
#         __table_args__ = {'schema': SCHEMA}

#     restaurant_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("restaurants.id")), primary_key=True)
#     type_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("restaurant_types.id")), primary_key=True)

restaurant_type_associations = db.Table(
    "restaurant_type_associations",
    db.Model.metadata,
    db.Column('restaurant_id',db.Integer, db.ForeignKey(add_prefix_for_prod("restaurants.id")), primary_key=True),
    db.Column('type_id',db.Integer, db.ForeignKey(add_prefix_for_prod("restaurant_types.id")), primary_key=True)
)
if environment == "production":
    restaurant_type_associations.schema = SCHEMA

class RestaurantType(db.Model):
    __tablename__ = "restaurant_types"
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    imageUrl = db.Column(db.String)

    restaurant = db.relationship("Restaurant", secondary="restaurant_type_associations", back_populates="types",)

    def to_dict(self):
        return {
            'id': self.id,
            "name": self.name,
            'imageUrl': self.imageUrl
        }