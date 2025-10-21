from flask import Blueprint, render_template
from models.db import db
from models.users import User

routes_users = Blueprint('routes_users', __name__, url_prefix='/users')

@routes_users.route('/')
def get_users():
    users = User.query.all()
    return render_template('dashboard.html', users=users)

@routes_users.route('/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return f"User {user_id} deleted"

@routes_users.route('/update/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    return f"User {user_id} updated"

@routes_users.route('/create', methods=['POST'])
def create_user():
    return "User created"

