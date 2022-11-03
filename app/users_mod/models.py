from app import db
from flask import sessions

class Base(db.Model):
    __abstract__ = True

    id  = db.Column(db.Integer, primary_key=True) 
    created_at = db.Column(db.DateTime(timezone=True),
                            default=db.func.current_timestamp()
                            )
    updated_at = db.Column(db.DateTime(timezone=True), 
                            default=db.func.current_timestamp(),
                            onupdate=db.func.current_timestamp()
                            )


class Users(Base):
    __tablename__ = 'users'

    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    is_active = db.Column(db.Boolean, nullable= False)
    