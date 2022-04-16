import json
import sys

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app import db
from app.board.forms import BoardForm
from app.board.models import Board, BoardPermission
from app.constants import *

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_board = Blueprint('board', __name__, url_prefix='/board')


@mod_board.route('/create', methods=['POST'])
@jwt_required()
def create():

    current_user = json.loads(get_jwt_identity())

    form = BoardForm(request.form, meta={'csrf': False})

    db.session.begin()

    try:

        # db.session.add(transaction)
        board = Board(name=form.board_name.data)
        db.session.add(board)

        db.session.flush()

        board_permission = BoardPermission(
            board_id=board.id, user_id=current_user['id'], permission=(1 << PERMISSION_ADMIN) + (1 << PERMISSION_OWNER))
        db.session.add(board_permission)

        db.session.commit()

        return jsonify(board_id=board.id)

    except:
        db.session.rollback()

        _, error_message, _ = sys.exc_info()

        return jsonify(error=error_message)


@mod_board.route('/edit', methods=['POST'])
@jwt_required()
def edit():

    current_user = json.loads(get_jwt_identity())

    board_id = request.form.get('board_id')

    permission = BoardPermission.query.filter_by(
        board_id=board_id, user_id=current_user['id']).first()

    if not (permission.permission & (1 << PERMISSION_ADMIN)):
        return jsonify(error="No permission")

    form = BoardForm(request.form, meta={'csrf': False})

    board = Board.query.filter_by(id=board_id).one()

    board.name = form.board_name.data

    db.session.commit()

    return jsonify(board_name=board.name)


@mod_board.route('/front/<board_id>', methods=['GET'])
@jwt_required(optional=True)
def get_one(board_id):

    board = Board.query.filter_by(id=board_id).one()

    user = get_jwt_identity()

    if (user):

        user = json.loads(user)

        board_permission = BoardPermission.query.filter_by(
            board_id=board_id, user_id=user['id']).first()

        permission = board_permission.permission if board_permission else 0

        return jsonify(board_name=board.name, board_permission=permission)

    return jsonify(board_name=board.name)
