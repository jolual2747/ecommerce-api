from sqlalchemy import Column, Integer, Float, String
from app.config.database import Base

class ProductModel(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    description =  Column(String)
    rating =  Column(Float)
    cost = Column(Float)