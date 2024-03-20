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
    "Other"
]

class Restaurant(db.Model):
    __tablename__ = "restaurants"
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    imageUrl = db.Column(db.String)
    createdAt = db.Column(db.Date, default=dt.datetime.now())
    updatedAt = db.Column(db.Date, default=dt.datetime.now())

    reviews = db.relationship("Review", back_populates="restaurant", cascade='all, delete-orphan')
    menu_items = db.relationship("MenuItem", back_populates="restaurant", cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            "name": self.name,
            'owner_id': self.owner_id,
            'location': self.location,
            'type': self.type,
            'reviews': [review.to_dict() for review in self.reviews],
            'imageUrl': self.imageUrl
        }
