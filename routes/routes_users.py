from flask import Blueprint, render_template, redirect, request, url_for
from models.db import db
from models.users import User
from utils.decorators import login_required, admin_required

routes_users = Blueprint('routes_users', __name__, url_prefix='/users')

#Funcion CRUD users

#Read
@routes_users.route('/')
@login_required
def get_users():
    users = User.query.all()
    return render_template('users/users.html', users=users)

#Delete
@routes_users.route('/delete/<int:id>')
@login_required
@admin_required
def delete_user(id):
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for('routes_users.get_users'))

#Update
@routes_users.route('/update/<int:id>', methods=['GET'])
def edit_user(id):
    user = User.query.get(id)
    return render_template('users/edit_user.html', user=user)

@routes_users.route('/update/<int:id>', methods=['POST'])
def update_user(id):
    user = User.query.get(id)
    user.username = request.form['username']
    user.email = request.form['email']
    user.password = request.form['password']
    user.role = request.form['role']
    db.session.commit()

    return redirect(url_for('routes_users.get_users'))


#Create
@routes_users.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return render_template('users/register.html', error="El usuario ya existe")

        new_user = User(username=username, password=password, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('routes_auth.login'))

    return render_template('users/register.html')

