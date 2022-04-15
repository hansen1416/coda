import json
import sys
# Import flask dependencies
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

# Import the database object from the main app module
from app import db

# Import module forms
from app.board.forms import BoardForm

# Import module models (i.e. User)
from app.board.models import Board

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_board = Blueprint('board', __name__, url_prefix='/board')

# Set the route and accepted methods


@mod_board.route('/create', methods=['POST'])
@jwt_required()
def create():

    board_name = request.form.get('board_name')

    current_user = json.loads(get_jwt_identity())

    form = BoardForm(request.form, meta={'csrf': False})

    db.session.begin()

    try:

        # db.session.add(transaction)
        board = Board(name=form.board_name.data)
        db.session.add(board)

        db.session.commit()

        return jsonify(board_id=board.id)

    except:
        db.session.rollback()

        _, error_message, _ = sys.exc_info()

        return jsonify(error=error_message)
