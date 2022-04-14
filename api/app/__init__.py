from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

jwt = JWTManager()

# Define the WSGI application object
app = Flask(__name__)


# Configurations
app.config.from_object('config')

CORS(app)
jwt.init_app(app)

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling


@app.errorhandler(404)
def not_found(error):
    return jsonify(error="404")


# Import a module / component using its blueprint handler variable (mod_auth)

def register_module():
    from app.auth.controllers import mod_auth as auth_module
    from app.board.controllers import mod_board as board_module

    # Register blueprint(s)
    app.register_blueprint(auth_module)
    app.register_blueprint(board_module)
    # ..

    # Build the database:
    # This will create the database file using SQLAlchemy
    db.create_all()


register_module()
