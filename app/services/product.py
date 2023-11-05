from app.models.product import ProductModel
from app.schemas.product import Product

class ProductService():
    def __init__(self, db):
        self.db = db

    def get_products(self):
        """Return all the products in database."""
        results = self.db.query(ProductModel).all()
        return results
    
    def get_product_by_id(self, id: int):
        """Return a product by id."""
        results = self.db.query(ProductModel).filter(ProductModel.id == id).first()
        return results
    
    def get_products_by_category(self, category:str):
        """Return products by category."""
        results = self.db.query(ProductModel).filter(ProductModel.category == category).all()
        return results
    
    def register_product(self, product:Product):
        """Register a new product."""
        product_dict = product.model_dump()
        if product_dict["id"]:
            product_dict.pop("id")

        new_product = ProductModel(**product_dict)
        self.db.add(new_product)
        self.db.commit()
