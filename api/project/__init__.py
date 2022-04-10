import os

from flask import Flask, jsonify
# from flask_sqlalchemy import SQLAlchemy
import psycopg2

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

    conn = get_db_connection()

    return jsonify(hello="world")
