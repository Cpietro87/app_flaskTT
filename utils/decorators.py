from functools import wraps
from flask import session, redirect, url_for, flash

# Decorators login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Necesitás credenciales para realizar esta acción.', 'warning')
            return redirect(url_for('routes_auth.login'))
        return f(*args, **kwargs)
    return decorated_function


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('role') != 'admin':
            flash('No tenés permisos de administrador para realizar esta acción.', 'danger')
            return redirect(url_for('routes_users.get_users'))
        return f(*args, **kwargs)
    return decorated_function
