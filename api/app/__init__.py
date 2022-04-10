from app.mod_auth.controllers import mod_auth as auth_module
from flask import Flask, jsonify
from flask_cors import CORS
from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)
CORS(app)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling


@app.errorhandler(404)
def not_found(error):
    return jsonify(error="404")


# Import a module / component using its blueprint handler variable (mod_auth)

# Register blueprint(s)
app.register_blueprint(auth_module)
# app.register_blueprint(xyz_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
