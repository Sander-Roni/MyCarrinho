from fastapi import FastAPI
from Models.EcommerceModel import base,database

base.metadata.create_all(bind=database)
app = FastAPI()


from Routers.Carrinho import RotaCarrinho
from Routers.Produtos import RouterProducts


app.include_router(RotaCarrinho)
app.include_router(RouterProducts)
