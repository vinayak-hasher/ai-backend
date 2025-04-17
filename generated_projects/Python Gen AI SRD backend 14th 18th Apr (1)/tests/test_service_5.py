```
import pytest
from your_app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_admin_access_granted(client):
    # Arrange
    headers = {'Authorization': 'Bearer admin_token'}
    # Act
    response = client.get('/api/admin_only', headers=headers)
    # Assert
    assert response.status_code == 200

def test_user_access_denied(client):
    # Arrange
    headers = {'Authorization': 'Bearer user_token'}
    # Act
    response = client.get('/api/admin_only', headers=headers)
    # Assert
    assert response.status_code == 403

def test_no_access_denied(client):
    # Act
    response = client.get('/api/admin_only')
    # Assert
    assert response.status_code == 401

def test_invalid_token(client):
    # Arrange
    headers = {'Authorization': 'Bearer invalid_token'}
    # Act
    response = client.get('/api/admin_only', headers=headers)
    # Assert
    assert response.status_code == 401
```