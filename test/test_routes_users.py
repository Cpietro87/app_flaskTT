import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from models.db import db
from app import app
from models.users import User 

@pytest.fixture
def client():

    with app.test_client() as client:
        with app.app_context():
            db.create_all()

            # Crear usuarios de prueba
            user1 = User(username="pietro", email="pietro@example.com", password="password123")
            user2 = User(username="maria", email="maria@example.com", password="password456")
            db.session.add_all([user1, user2])
            db.session.commit()

        yield client

        # Limpiar después del test
        with app.app_context():
            db.drop_all()


def test_get_users_route(client):
    """Verifica que la ruta /users devuelva el template y datos correctos"""
    response = client.get('/users/')
    assert response.status_code == 200

    # El HTML debe incluir los nombres de los usuarios insertados
    html = response.data.decode('utf-8')
    assert "pietro" in html
    assert "maria" in html

