import json
# Import flask dependencies
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

# Import the database object from the main app module
from app import db

# Import module forms
from app.auth.forms import RegisterForm

# Import module models (i.e. User)
from app.auth.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_board = Blueprint('board', __name__, url_prefix='/board')

# Set the route and accepted methods


@mod_board.route('/create', methods=['POST'])
@jwt_required()
def get_me():

    board_name = request.form.get('board_name')

    current_user = json.loads(get_jwt_identity())

    return jsonify(board_name=board_name, id=current_user['id'])
