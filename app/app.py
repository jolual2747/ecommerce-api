from fastapi import FastAPI
from app.config.database import Base, engine
from app.routers.product import products_router
from app.routers.auth import auth_router
from fastapi.responses import HTMLResponse

app = FastAPI()

Base.metadata.create_all(bind = engine)

routers = [auth_router, products_router]

for router in routers:
    app.include_router(router)

@app.get('/home', tags=['home'])
def home():
    return HTMLResponse('<h1>Welcome!</h1>')