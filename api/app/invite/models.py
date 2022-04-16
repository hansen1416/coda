# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db
from sqlalchemy.orm.exc import NoResultFound
from app.constants import *


# Define a User model
class Invite(db.Model):

    __tablename__ = 'invite'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    board_id = db.Column(db.Integer,  nullable=False)

    sender_user_id = db.Column(db.Integer,  nullable=False)

    receiver_user_id = db.Column(db.Integer,  nullable=False)

    status = db.Column(db.SmallInteger,  nullable=False,
                       default=INVITE_DEFAULT, comment="default:0, accpeted:1, rejected:2")

    created_at = db.Column(db.DateTime,  default=db.func.current_timestamp())

    # New instance instantiation procedure
    def __init__(self, board_id, sender_user_id, receiver_user_id):
        self.board_id = board_id
        self.sender_user_id = sender_user_id
        self.receiver_user_id = receiver_user_id
