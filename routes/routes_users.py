from flask import Blueprint, render_template, redirect, request, url_for
from models.db import db
from models.users import User

routes_users = Blueprint('routes_users', __name__, url_prefix='/users')

@routes_users.route('/')
def get_users():
    users = User.query.all()
    return render_template('users/users.html', users=users)

@routes_users.route('/delete/<int:id>')
def delete_user(id):
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for('routes_users.get_users'))

@routes_users.route('/update/<int:id>', methods=['GET'])
def edit_user(id):
    user = User.query.get(id)
    return render_template('users/edit_user.html', user=user)

@routes_users.route('/update/<int:id>', methods=['POST'])
def update_user(id):
    return f"User {id} updated"

@routes_users.route('/register')
def register():
    return render_template('users/register.html')

