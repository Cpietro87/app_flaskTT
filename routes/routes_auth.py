from flask import Blueprint, render_template


routes_auth = Blueprint('routes_auth', __name__,)

@routes_auth.route('/login', methods=['GET'])
def login():
    return render_template('users/login.html')