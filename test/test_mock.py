import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from unittest.mock import patch, MagicMock
from app import app
from models.users import User


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        with app.app_context():
            yield client


def test_get_users_with_mock(client):
    """Test unitario que mockea la consulta y el render sin tocar DB"""
    fake_users = [
        User(username="pietro", email="pietro@example.com", password="123"),
        User(username="maria", email="maria@example.com", password="456"),
    ]

    # Mock directo al objeto importado en el módulo routes_users
    with patch("routes.routes_users.User") as mock_user:
        mock_user.query.all.return_value = fake_users

        # Mock del render_template para no cargar HTML real
        with patch("routes.routes_users.render_template") as mock_render:
            mock_render.return_value = "render ok"

            response = client.get("/users/")

            # Verificaciones
            mock_user.query.all.assert_called_once()
            mock_render.assert_called_once_with("users/users.html", users=fake_users)
            assert response.status_code == 200
            assert b"render ok" in response.data


