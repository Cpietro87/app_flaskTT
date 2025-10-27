from flask import Blueprint, render_template, request, redirect, url_for, session
from models.users import User

routes_auth = Blueprint('routes_auth', __name__,)

@routes_auth.route('/login', methods=['GET', 'POST'] )
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['username'] = user.username
            session['role'] = user.role
            return redirect(url_for('routes_users.get_users'))
        else:
            return render_template('users/login.html', error="Credenciales inválidas")
    return render_template('users/login.html')

@routes_auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('routes_auth.login'))
