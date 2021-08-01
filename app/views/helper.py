import datetime

from marshmallow.fields import String
from app.views.users import user_by_email
from app import app
import jwt
from werkzeug.security import check_password_hash
from flask import json, request, jsonify
from functools import wraps

def auth():
    email = request.json['email']
    password = request.json['password']

    if not email or not password:
        return jsonify({
            'message': 'could not verify',
            'Authenticate': 'Invalid data'
        }), 401
    
    user = user_by_email(email)
    if not user:
        return jsonify({
            'message': 'user not found',
            'data': {}
        }), 401

    if user and check_password_hash(user.password, password):
        token = jwt.encode({"email": user.email, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12)}, app.config['SECRET_KEY'], algorithm="HS256")
        
        return jsonify({
            'message': 'Validate successfully',
            'token': token,
            'exp': datetime.datetime.now() + datetime.timedelta(hours=12)
        })

    return jsonify({
        'message': 'could not verify',
        'Authenticate': 'Invalid data'
    }), 401

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        authToken = request.headers.get('Authorization')
        token = authToken.replace("Bearer", "").strip()
        if not token:
            return jsonify({
                'message': 'token is missing',
                'data': {}
            }), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = user_by_email(email=data['email'])
        except:
            return jsonify({
                'message': 'token is invalid or expider',
                'data': {}
            }), 401
        return f(current_user, *args, **kwargs)
    return decorated