#!/usr/bin/env python3
""" module for session auth view """
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'],
strict_slashes=False)
def auth_session():
    """ authentication session """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({ "error": "email missing" }), 400

    if not password:
        return jsonify({ "error": "password missing" }), 400

    try:
        _user = User.search({'email': email})
    except Exception:
        _user = []

    if len(_user) > 0:
        valid_pass = _user[0].is_valid_password(password)
        if not valid_pass:
                return jsonify({"error": "wrong password"}), 401

        from api.v1.app import auth
        session_id = auth.create_session(_user[0].id)
        _user_json = jsonify(_user[0].to_json())
        _cookie = os.getenv('SESSION_NAME')
        _user_json.set_cookie(_cookie, session_id)
        return _user_json
    else:
        return jsonify({"error": "no user found for this email"}), 404
