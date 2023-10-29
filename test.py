from app.schemas.product import Product

prod = Product(id= 1,  name= "mouse", category = "tech", description= "Wireless mouse for PC",  rating= 4.5,  cost= 5)

dictt =prod.model_dump()
if dictt["id"]:
    dictt.pop("id")

print(dictt)