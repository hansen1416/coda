# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db


# Define a User model
class Post(db.Model):

    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    board_id = db.Column(db.Integer,  nullable=False)

    user_id = db.Column(db.Integer,  nullable=False)

    thread_id = db.Column(db.Integer,  nullable=False)

    content = db.Column(db.Text,  nullable=False)

    created_at = db.Column(db.DateTime,  default=db.func.current_timestamp())

    # updated_at = db.Column(db.DateTime,  default=db.func.current_timestamp())

    # New instance instantiation procedure
    def __init__(self, board_id, user_id, thread_id, content):
        self.board_id = board_id
        self.user_id = user_id
        self.thread_id = thread_id
        self.content = content
