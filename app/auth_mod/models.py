# data models for the Authorization module
from app import db

# Base model for database tables to inherit
class BASE(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.DateTime())