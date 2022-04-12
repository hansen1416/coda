import json
# Import flask dependencies
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

# Import password / encryption helper tools
from werkzeug.security import check_password_hash

# Import the database object from the main app module
from app import db

# Import module forms
from app.auth.forms import RegisterForm

# Import module models (i.e. User)
from app.auth.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

# Set the route and accepted methods


@mod_auth.route('/register', methods=['POST'])
def register():

    email = User.query.filter_by(
        email=request.form.get('email')).first()

    if email:
        return jsonify(error="email taken")

    username = User.query.filter_by(
        username=request.form.get('username')).first()

    if username:
        return jsonify(error="username taken")

    # If sign in form is submitted
    form = RegisterForm(request.form, meta={'csrf': False})

    # Verify the sign in form
    if form.validate_on_submit():

        user = User(username=form.username.data,
                    email=form.email.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()

        access_token = create_access_token(
            identity=json.dumps({"id": user.id, "username": user.username, "email": user.email}))

        return jsonify(access_token=access_token)

    for fieldName, errorMessages in form.errors.items():
        for err in errorMessages:
            print(err)

    return jsonify(error=" ".join(form.username.errors) + " ".join(form.email.errors))


@mod_auth.route('/login', methods=['POST'])
def login():

    user = User.query.filter_by(email=request.form.get('email')).first()

    if user and check_password_hash(user.password, request.form.get('password')):
        access_token = create_access_token(
            identity=json.dumps({"id": user.id, "username": user.username, "email": user.email}))
        return jsonify(access_token=access_token)

    return jsonify(error="failed")


@mod_auth.route('/me', methods=['GET'])
@jwt_required()
def get_me():

    current_user = get_jwt_identity()

    return jsonify(current_user=current_user)
