# Import flask dependencies
from flask import Blueprint, request, jsonify, session

# Import password / encryption helper tools
from werkzeug.security import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db

# Import module forms
from app.mod_auth.forms import RegisterForm

# Import module models (i.e. User)
from app.mod_auth.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

# Set the route and accepted methods


@mod_auth.route('/register', methods=['POST'])
def register():

    # If sign in form is submitted
    form = RegisterForm(request.form)

    # Verify the sign in form
    if form.validate_on_submit():

        user = User(username=form.username.data,
                    email=form.email.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()

        return jsonify(id=user.id)

    return jsonify(error="failed")
