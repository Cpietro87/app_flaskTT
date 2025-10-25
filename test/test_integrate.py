import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import app
from models.db import db
from models.users import User
from config.config import DATABASE_CONNECTION_URI

# Context
@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    with app.app_context():
        db.create_all()
        # Insertar datos de prueba
        user = User(username="pietro", email="pietro@example.com", password="123")
        db.session.add(user)
        db.session.commit()
    yield app.test_client()
    # Limpieza
    with app.app_context():
        db.drop_all()

# Test
def test_get_users(client):
    response = client.get('/users/')
    assert response.status_code == 200
    assert b"pietro" in response.data

