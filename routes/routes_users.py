from flask import Blueprint, render_template, redirect, request, url_for
from models.db import db
from models.users import User

routes_users = Blueprint('routes_users', __name__, url_prefix='/users')

#Funcion CRUD users

#Read
@routes_users.route('/')
def get_users():
    users = User.query.all()
    return render_template('users/users.html', users=users)

#Delete
@routes_users.route('/delete/<int:id>')
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
    db.session.commit()

    return redirect(url_for('routes_users.get_users'))


#Create
@routes_users.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username =request.form['username']
        email = request.form['email']
        password = request.form['password']

        existing_user = User.query.filter((User.email == email)).first()
        if existing_user:
            return render_template('users/register.html', error="User already exists") 
        
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('routes_users.get_users'))

    return render_template('users/register.html')

