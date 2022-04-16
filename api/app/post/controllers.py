import json
import sys

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app import db
from app.thread.models import ThreadPermission
from app.post.models import Post
from app.constants import *

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_post = Blueprint('post', __name__, url_prefix='/post')


@mod_post.route('/add', methods=['POST'])
@jwt_required()
def add():

    current_user = json.loads(get_jwt_identity())

    user_id = current_user['id']
    board_id = request.form.get('board_id')
    thread_id = request.form.get('thread_id')
    content = request.form.get('content')

    post = Post(
        board_id=board_id,
        user_id=user_id,
        thread_id=thread_id,
        content=content,
    )

    db.session.add(post)
    db.session.commit()

    return jsonify(thread_id=thread_id)


@mod_post.route('/update', methods=['POST'])
@jwt_required()
def update():

    current_user = json.loads(get_jwt_identity())

    user_id = current_user['id']
    board_id = request.form.get('board_id')
    thread_id = request.form.get('thread_id')
    post_id = request.form.get('post_id')
    content = request.form.get('content')

    if not ThreadPermission.has_permission(board_id, thread_id, user_id):
        return jsonify(error="No permission")

    post = Post.query.filter_by(id=post_id).one()

    post.content = content

    db.session.commit()

    return jsonify(post_id=post_id)


@mod_post.route('/delete', methods=['POST'])
@jwt_required()
def update():

    current_user = json.loads(get_jwt_identity())

    user_id = current_user['id']
    board_id = request.form.get('board_id')
    thread_id = request.form.get('thread_id')
    post_id = request.form.get('post_id')

    if not ThreadPermission.has_permission(board_id, thread_id, user_id):
        return jsonify(error="No permission")

    Post.query.filter_by(id=post_id).delete()

    db.session.commit()

    return jsonify(thread_id=thread_id)
