from werkzeug.security import generate_password_hash
from app import db
from flask import json, request, jsonify
from ..models.users import Users, user_schema, users_schema

def get_users():
    users = Users.query.all()
    if users:
        result = users_schema.dump(users)
        return jsonify({ 'message': 'successfully fetched', 'data': result })
    
    return jsonify({'message': 'nothin found', data: {}})

def get_user(id):
    user = Users.query.get(id)
    if user:
        result = user_schema.dump(user)
        return jsonify({'message': 'successfylly fetched', 'data': result})
    return jsonify({ 'message': 'unable to create', 'data': {}}), 404

def post_user():
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    email = request.json['email']

    pass_hash = generate_password_hash(password)
    user = Users(username, pass_hash, email, name)

    try:
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({ 'message': 'successfuly refistered', 'data': result }), 201
    except:
        return jsonify({ 'message': 'unable to create', 'data': {}}), 500

def update_user(id):
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    email = request.json['email']

    user = Users.query.get(id)

    if not user:
        return jsonify({'message': 'user does not exists', 'data': {}}), 404

    pass_has = generate_password_hash(password)

    try:
        user.username = username
        user.email = email
        user.password = pass_has
        user.name = name

        db.session.commit()
        result = user_schema.dump(user)

        return jsonify({ 'message': 'successfuly refistered', 'data': result }), 200
    except:
        return jsonify({ 'message': 'unable to create', 'data': {}}), 500


def delete_user(id):
    user = Users.query.get(id)

    if not user:
        return jsonify({'message': 'user does not exists', 'data': {}}), 404
    
    if user:
        try:
            db.session.delete(user)
            db.session.commit()
            result = user_schema.dump(user)

            return jsonify({
                'message': 'successfully deleted',
                'data': result
            }), 200
        except:
            return jsonify({
                'message': 'unable to delete',
                'data': {}
            }), 500

def user_by_email(email):
    try:
        return Users.query.filter(Users.email == email).one()
    except:
        return None