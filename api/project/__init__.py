import os

# from flask_sqlalchemy import SQLAlchemy
from flask import {Flask, jsonify, request}
import psycopg2
from werkzeug.security import safe_str_cmp

app = Flask(__name__)
# read config from config.py
app.config.from_object("project.config.Config")
# db = SQLAlchemy(app)


# class User(db.Model):
#     __tablename__ = "users"

#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(128), unique=True, nullable=False)
#     active = db.Column(db.Boolean(), default=True, nullable=False)

#     def __init__(self, email):
#         self.email = email

def get_db_connection():
    conn = psycopg2.connect(host='db',
                            database='coda',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn


@app.route("/")
def hello_world():

    return jsonify(hello="world")


@app.route("/register")
def register():

    username = request.form.get('username')
    password = request.form.get('password')

    return jsonify(username=username, password=password)
