# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db
from app.constants import *
from app.board.models import BoardPermission

# Define a User model


class Thread(db.Model):

    __tablename__ = 'thread'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    board_id = db.Column(db.Integer,  nullable=False)

    user_id = db.Column(db.Integer,  nullable=False)

    title = db.Column(db.String(128),  nullable=False)

    created_at = db.Column(db.DateTime,  default=db.func.current_timestamp())

    # New instance instantiation procedure
    def __init__(self, board_id, user_id, title):
        self.board_id = board_id
        self.user_id = user_id
        self.title = title


class ThreadPermission(db.Model):

    __tablename__ = 'thread_permission'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    board_id = db.Column(db.Integer, nullable=False)

    thread_id = db.Column(db.Integer, nullable=False)

    user_id = db.Column(db.Integer, nullable=False)

    permission = db.Column(db.Integer, nullable=False)

    def __init__(self, board_id, thread_id, user_id, permission):
        self.board_id = board_id
        self.thread_id = thread_id
        self.user_id = user_id
        self.permission = permission

    def has_permission(board_id, thread_id, user_id):

        board_permission = BoardPermission.query.filter_by(
            board_id=board_id, user_id=user_id).one()

        if board_permission:
            if board_permission.permission & (1 << PERMISSION_ADMIN):
                return True

            if board_permission.permission & (1 << PERMISSION_MOD):
                return True

        thread_permission = ThreadPermission.query.filter_by(
            thread_id=thread_id, user_id=user_id).one()

        if not thread_permission:
            return False

        if thread_permission.permission & (1 << PERMISSION_ADMIN):
            return True

        if thread_permission.permission & (1 << PERMISSION_MOD):
            return True

        return False
