import json
import urllib.request

# Import flask dependencies
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, \
    jwt_required, get_jwt_identity

# Import password / encryption helper tools
from werkzeug.security import check_password_hash

from app import db
from app.auth.forms import RegisterForm
from app.auth.models import User
from app.gravartar import Gravatar

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

        user_json = json.dumps(
            {"id": user.id, "username": user.username, "email": user.email})

        access_token = create_access_token(identity=user_json)
        refresh_token = create_refresh_token(identity=user_json)

        return jsonify(access_token=access_token, refresh_token=refresh_token)

    for fieldName, errorMessages in form.errors.items():
        for err in errorMessages:
            print(err)

    return jsonify(error=" ".join(form.username.errors) + " ".join(form.email.errors))


@mod_auth.route('/login', methods=['POST'])
def login():

    user = User.query.filter_by(email=request.form.get('email')).first()

    if user and check_password_hash(user.password, request.form.get('password')):
        user_json = json.dumps(
            {"id": user.id, "username": user.username, "email": user.email})

        access_token = create_access_token(identity=user_json)
        refresh_token = create_refresh_token(identity=user_json)

        return jsonify(access_token=access_token, refresh_token=refresh_token)

    return jsonify(error="failed")


@mod_auth.route('/refresh', methods=['GET'])
@jwt_required(refresh=True, optional=True)
def refresh_me():

    current_user = get_jwt_identity()

    req = urllib.request.Request("http://worker:5000", data={})

    resp = urllib.request.urlopen(req)

    print(resp)

    if current_user:

        access_token = create_access_token(identity=current_user)
        refresh_token = create_refresh_token(identity=current_user)

        current_user = json.loads(current_user)
        g = Gravatar(current_user['email'])

        current_user['avartar'] = g.get_image()

        return jsonify(current_user=current_user, access_token=access_token, refresh_token=refresh_token)

    return jsonify(current_user="", access_token="", refresh_token="")


@mod_auth.route('/me', methods=['GET'])
@jwt_required(optional=True)
def me():

    current_user = get_jwt_identity()

    if current_user:
        current_user = json.loads(current_user)
        g = Gravatar(current_user['email'])

        current_user['avartar'] = g.get_image()

        return jsonify(current_user=current_user)

    return jsonify(current_user={})
