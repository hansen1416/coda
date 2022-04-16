import json
import sys

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app import db
from app.auth.models import User
from app.board.models import BoardPermission
from app.invite.models import Invite
from app.constants import *

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_invite = Blueprint('invite', __name__, url_prefix='/invite')


@mod_invite.route('/add', methods=['POST'])
@jwt_required()
def add():

    current_user = json.loads(get_jwt_identity())

    sender_user_id = current_user['id']

    receiver = User.query.filter_by(
        username=request.form.get('username')).one()

    if not receiver:
        return jsonify(error="Invalid username")

    board_id = request.form.get('board_id')

    board_permission = BoardPermission.query.filter_by(
        board_id=board_id, user_id=sender_user_id).one()

    if not board_permission or not board_permission.permission & (1 << PERMISSION_ADMIN):
        return jsonify(error="No permission")

    invite = Invite(board_id=board_id, sender_user_id=sender_user_id,
                    receiver_user_id=receiver.id)

    db.session.add(invite)
    db.session.commit()

    return jsonify(invite=invite.receiver_user_id)


@mod_invite.route('/update', methods=['POST'])
@jwt_required()
def update():

    current_user = json.loads(get_jwt_identity())

    invite_id = request.form.get('invite_id')

    with db.session.begin():

        try:

            invite = Invite.query.filter_by(id=invite_id).one()

            if invite.receiver_user_id != current_user['id']:
                return jsonify(error="No permission")

            status = int(request.form.get('status'))

            invite.status = status

            permission = 0

            if status == INVITE_ACCEPT:
                board_permission = BoardPermission.query.filter_by(board_id=request.form.get('board_id'),
                                                                   user_id=current_user['id']).first()

                if board_permission:
                    board_permission.permission = board_permission.permission + \
                        (1 << PERMISSION_MOD)
                else:
                    board_permission = BoardPermission(board_id=request.form.get('board_id'),
                                                       user_id=current_user['id'],
                                                       permission=(1 << PERMISSION_MOD))

                    db.session.add(board_permission)

                permission = board_permission.permission

            db.session.commit()

            return jsonify(permission=permission)

        except:
            db.session.rollback()

            _, error_message, _ = sys.exc_info()

            return jsonify(error=error_message)
