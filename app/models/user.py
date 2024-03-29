from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.orm import validates
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import re


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String, nullable=True)
    wallet = db.Column(db.Float, nullable=True, default =0)
    order_id = db.Column(db.Integer, default=1)

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    # @validates("name")
    # def validate_name(self):
    #     specialChars = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    #     if (specialChars.search(self.name) != None):
    #         raise ValueError("Name must only have alpha-numeric characters")
    #     return self.name

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict_private(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            "order_id": self.order_id,
            "wallet": self.wallet
        }

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            "order_id": self.order_id
        }
