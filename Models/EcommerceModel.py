from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine, Column, String, Float, Date, Integer,ForeignKey

database = create_engine("sqlite:///BancoEcommerce.db")
base = declarative_base()

class Produto(base):
    __tablename__ = "produtos"

    id = Column("id",Integer,primary_key=True,autoincrement=True)
    Nome = Column("Nome",String)
    Ean = Column("Ean",Integer)
    Preco = Column("Preco",Float)
    Estoque = Column("Estoque",Integer)


class LoteProduto(base):
    __tablename__ = "LoteCommerce"

    id = Column("id",Integer,primary_key=True,autoincrement=True)
    produto_id = Column("produto_id",Integer)
    DataDeFabricacao = Column("DataDeFabricacao",Date)
    Validade = Column("Validade",Date)
    MatrizDoProduto = Column("MatrizDoProduto",String)


class ItemPedido(base):
    __tablename__ = "ItemPedido"

    id = Column("id",Integer,primary_key=True,autoincrement=True)
    produto_id = Column("produto_id",Integer, ForeignKey("produtos.id"))
    pedido_id = Column(Integer, ForeignKey("Pedido.id"))
    quantidade = Column("quantidade",Integer)
    preco_unitario = Column("preco_unitario",Float)
    pedido = relationship("Pedido", back_populates="itens")


class ItemCarrinho(base):
    __tablename__ = "itens_carrinho"

    id = Column("id",Integer,primary_key=True,autoincrement=True)
    carrinho_id = Column(Integer,ForeignKey("CarrinhoCommerce.id"))
    produto_id = Column(Integer,ForeignKey("produtos.id"))
    quantidade = Column(Integer)
    preco_unitario = Column(Integer)
    carrinho = relationship("Carrinho",back_populates="itens")

class Carrinho(base):
    __tablename__ = "CarrinhoCommerce"

    id = Column("id",Integer,primary_key=True,autoincrement=True)
    itens = relationship("ItemCarrinho",back_populates="carrinho")

class Pedido(base):
    __tablename__ = "Pedido"

    id = Column("id",Integer,primary_key=True,autoincrement=True)
    itens = relationship("ItemPedido",back_populates="pedido")