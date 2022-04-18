# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db
from sqlalchemy import event, DDL
from sqlalchemy.orm.exc import NoResultFound
from werkzeug.security import check_password_hash, generate_password_hash


# Define a User model
class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # User Name
    username = db.Column(db.String(128),  nullable=False)

    # Identification Data: email & password
    email = db.Column(db.String(128),  nullable=False,
                      unique=True)
    password = db.Column(db.String(192),  nullable=False)

    created_at = db.Column(db.DateTime,  default=db.func.current_timestamp())

    # New instance instantiation procedure
    def __init__(self, username, email, password):

        self.username = username
        self.email = email
        self.set_password(password)

    # strings based on the state of the object, if __str__ is missing
    def __repr__(self):
        return '<User %r>' % (self.username)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @classmethod
    def get(cls, user_id):

        try:
            return User.query.filter_by(id=user_id).one()
        except NoResultFound:
            return None


class Superusers(db.Model):

    __tablename__ = 'superusers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    user_id = db.Column(db.Integer, nullable=False)

    assigner_id =

    # New instance instantiation procedure
    def __init__(self, user_id):
        self.user_id = user_id


# def after_superusers_create(target, connection, **kw):
#     connection.execute(text(
#         "ALTER TABLE %s SET name=foo_%s" % (target.name, target.name)
#     ))


event.listen(Superusers.__table__, "after_create", DDL(
    "INSERT INTO %(table)s (user_id) VALUES (1)"),)


# @event.listens_for(Superusers.__table__, 'after_create')
# def default_admin(*args, **kwargs):
#     db.session.add(Superusers(user_id=1))
#     db.session.commit()
