import json
import sys

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app import db
from app.thread.models import Thread, ThreadPermission
from app.post.models import Post
from app.constants import *

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_thread = Blueprint('thread', __name__, url_prefix='/thread')


@mod_thread.route('/read/<thread_id>', methods=['POST'])
@jwt_required(optional=True)
def read(thread_id):

    thread = Thread.query.filter_by(id=thread_id).one()

    board_id = thread.board_id

    posts = Post.query.filter_by(id=thread_id).all()

    permission = 0

    current_user = get_jwt_identity()

    if current_user:
        current_user = json.loads(current_user)
        user_id = current_user['id']

        permission = ThreadPermission.has_permission(
            board_id, thread_id, user_id)

    return jsonify(thread=thread.title, posts=posts, permission=int(permission))


@mod_thread.route('/add', methods=['POST'])
@jwt_required()
def add():

    current_user = json.loads(get_jwt_identity())

    user_id = current_user['id']
    board_id = request.form.get('board_id')
    title = request.form.get('title')
    content = request.form.get('content')

    with db.session.begin():
        try:
            thread = Thread(
                board_id=board_id,
                user_id=user_id,
                title=title
            )

            db.session.add(thread)

            db.session.flush()

            post = Post(
                board_id=board_id,
                user_id=user_id,
                thread_id=thread.id,
                content=content,
            )

            db.session.add(post)

            thread_permission = ThreadPermission(
                board_id=board_id,
                thread_id=thread.id,
                user_id=user_id,
                permission=(1 << PERMISSION_OWNER) + (1 << PERMISSION_ADMIN),
            )

            db.session.add(thread_permission)

            db.session.commit()

            return jsonify(thread_id=thread.id)

        except:
            db.session.rollback()

            _, error_message, _ = sys.exc_info()

            return jsonify(error=error_message)


@mod_thread.route('/delete', methods=['POST'])
@jwt_required()
def update():

    current_user = json.loads(get_jwt_identity())

    user_id = current_user['id']
    board_id = request.form.get('board_id')
    thread_id = request.form.get('thread_id')

    if not ThreadPermission.has_permission(board_id, thread_id, user_id):
        return jsonify(error="No permission")

    with db.session.begin():
        try:
            Thread.query.filter_by(id=thread_id).delete()

            Post.query.filter_by(thread_id=thread_id).delete()

            db.session.commit()

            return jsonify(info=1)
        except:
            db.session.rollback()

            _, error_message, _ = sys.exc_info()

            return jsonify(error=error_message)
