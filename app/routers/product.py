from fastapi import APIRouter, Query, Path, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.schemas.product import Product
from app.services.product import ProductService
from app.config.database import get_db, SessionLocal
from typing import List

products_router = APIRouter()

@products_router.get('/products', tags=['products'], response_model=List[Product])
def get_products(db: SessionLocal = Depends(get_db)) -> List[Product]:
    """Return all products."""
    results = ProductService(db).get_products()
    return JSONResponse(status_code=200, content=jsonable_encoder(results))

@products_router.get('/products/{id}', tags=['products'], response_model=Product, status_code=200)
def get_product_by_id(id:int = Path(ge=1), db: SessionLocal = Depends(get_db)) -> Product:
    """Return product by id."""
    results = ProductService(db).get_product_by_id(id)
    if results:
        return JSONResponse(status_code=200, content=jsonable_encoder(results))
    return JSONResponse(status_code=404, content={"message":"product not found"})

@products_router.get('/products/', tags=['products'], status_code=200, response_model=List[Product])
def get_products_by_category(category:str = Query(min_length=3, max_length=15), db: SessionLocal = Depends(get_db)) -> List[Product]:
    """Get all products by a category."""
    results = ProductService(db).get_products_by_category(category)
    print(results)
    print(type(results))
    if results:
        return JSONResponse(status_code=200, content=jsonable_encoder(products_router))
    return JSONResponse(status_code=404, content={"message":"product not found"})

@products_router.post('/products/', tags=['products'], status_code=201, response_model=dict)
def register_product(product:Product, db: SessionLocal = Depends(get_db)) -> dict:
    """Register new product.."""
    ProductService(db).register_product(product)
    return JSONResponse(status_code=201, content={"message":"Product succesfully registered"})
