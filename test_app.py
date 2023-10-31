from app.app import app
from fastapi.testclient import TestClient
from config import get_settings

client = TestClient(app)

def test_create_product():
    """Test to validate if a product is registered and checks authetication token"""
    settings = get_settings()
    product_to_register = {"category": "test", "cost": 0, "description": "test product", "name": "test", "rating": 0}
    access_token = client.post('/auth/login', data = {"username":settings.TEST_USER, "password":settings.TEST_PASSWORD})
    headers = {"Authorization": f"Bearer {access_token.json()['access_token']}"}
    response = client.post('/products/', json=product_to_register, headers=headers)
    assert response.status_code == 201
    assert response.json() == {"message":"Product succesfully registered"}