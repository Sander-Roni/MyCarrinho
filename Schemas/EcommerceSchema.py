from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import date

class ProdutoSchema(BaseModel):
    Nome : str 
    Ean : int 
    Preco : float
    Estoque : int

    class Config:
        from_attributes = True  

class LoteProdutoSchema(BaseModel):
    produto_id : int 
    DataDeFabricacao : Optional[date]
    Validade : Optional[date]
    MatrizDoProduto : str 

    class Config:
        from_attributes = True 

class ItemPedidoSchema(BaseModel):
    produto_id : int
    quantidade : int

    class Config:
        from_attributes = True 

class CarrinhoSchema(BaseModel):
    itens : list[ItemPedidoSchema]

    class Config:
        from_attributes = True 

class PedidoSchema(BaseModel):
    carrinho_id : int

class PedidoResponseSchema(BaseModel):
    id : int 
    total : float
    status : str 
    itens : list[ItemPedidoSchema] 

    class Config:
        from_attributes = True 

CarrinhoSchema
PedidoSchema
ProdutoSchema