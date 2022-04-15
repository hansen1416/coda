# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db
from sqlalchemy.orm.exc import NoResultFound


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
        return '<User %r>' % (self.name)

    @classmethod
    def get(cls, board_id):

        try:
            return Board.query.filter_by(id=board_id).one()
        except NoResultFound:
            return None