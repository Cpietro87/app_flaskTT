from models.db import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False) 
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(20), default='user', nullable=False)

    def __init__(self, username, password, email, role='user'):
        self.username = username
        self.password = password
        self.email = email
        self.role = role

    def set_password(self, password):
        """Genera un hash seguro para la contraseña."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verifica si la contraseña ingresada coincide con el hash guardado."""
        return check_password_hash(self.password_hash, password)


    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'role': self.role
        }
