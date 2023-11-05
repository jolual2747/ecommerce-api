#from app.app import app
from fastapi.testclient import TestClient
from config import get_settings
from app.schemas.product import Product

#client = TestClient(app)

# def test_create_product():
#     """Test to validate if a product is registered and checks authetication token"""
#     settings = get_settings()
#     product_to_register = {"category": "test", "cost": 0, "description": "test product", "name": "test", "rating": 0}
#     access_token = client.post('/auth/login', data = {"username":settings.TEST_USER, "password":settings.TEST_PASSWORD})
#     headers = {"Authorization": f"Bearer {access_token.json()['access_token']}"}
#     response = client.post('/products/', json=product_to_register, headers=headers)
#     assert response.status_code == 201
#     assert response.json() == {"message":"Product succesfully registered"}


def test_product():
    product = {"id": 1, "name": "mouse", "category": "tech", "description": "Wireless mouse for PC", "rating": 4.5, "cost": 5 }
    product_schema = Product(**product)
    assert product["id"] == product_schema.id
    assert product["name"] == product_schema.name
    assert product["category"] == product_schema.category
    assert product["description"] == product_schema.description
    assert product["rating"] == product_schema.rating
    assert product["cost"] == product_schema.cost