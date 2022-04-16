# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db
from sqlalchemy.orm.exc import NoResultFound
from app.constants import *

# Define a User model


class Board(db.Model):

    __tablename__ = 'board'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # Board Name
    name = db.Column(db.String(128),  nullable=False)

    created_at = db.Column(db.DateTime,  default=db.func.current_timestamp())

    # New instance instantiation procedure
    def __init__(self, name):
        self.name = name

    # strings based on the state of the object, if __str__ is missing
    def __repr__(self):
        return '<Board %r>' % (self.name)

    @classmethod
    def get(cls, board_id):

        try:
            return Board.query.filter_by(id=board_id).one()
        except NoResultFound:
            return None


class BoardPermission(db.Model):
    """
        Superuser: 1 << 1
        Board Administrators: 1 << 2
        Board Moderators: 1 << 3

    """

    __tablename__ = 'board_permission'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    board_id = db.Column(db.Integer, nullable=False)

    user_id = db.Column(db.Integer, nullable=False)

    permission = db.Column(db.Integer, nullable=False)

    def __init__(self, board_id, user_id, permission):
        self.board_id = board_id
        self.user_id = user_id
        self.permission = permission

    def has_permission(board_id, user_id):

        board_permission = BoardPermission.query.filter_by(
            board_id=board_id, user_id=user_id).first()

        if board_permission and board_permission.permission & (1 << PERMISSION_ADMIN):
            return True

        return False
