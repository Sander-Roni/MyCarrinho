from fastapi import APIRouter, Depends, HTTPException
from Models.EcommerceModel import Carrinho,ItemCarrinho,Produto
from Schemas.EcommerceSchema import CarrinhoSchema
from dependencies import SessionCommerce
from sqlalchemy.orm import Session

RotaCarrinho = APIRouter(prefix="/Carrinho", tags=["Meus Produtos"])

@RotaCarrinho.post("/")
async def CadastrarProduto(schema_carrinho : CarrinhoSchema, db: Session = Depends(SessionCommerce)):
    
    novo_carrinho = Carrinho()

    db.add(novo_carrinho)
    db.commit()
    db.refresh(novo_carrinho)

    total = 0

    for i in schema_carrinho.itens:
        produto = db.query(Produto).filter(Produto.id == i.produto_id).first()
        
        if not produto:
            raise HTTPException(status_code=404, detail="O Produto não foi encontrado...")
        
        subtotal = produto.Preco * i.quantidade
        total += subtotal

        novo_item = ItemCarrinho(
            carrinho_id = novo_carrinho.id,
            produto_id = i.produto_id,
            quantidade=i.quantidade
        )

        db.add(novo_item)
    db.commit()

    return {"mensagem":"Item Adicionado ao Carrinho com Sucesso!",
            "id":novo_carrinho.id,
            "total":total}


@RotaCarrinho.get("/")
async def ConsultarCarrinho(db : Session =  Depends(SessionCommerce)):
    
    carrinhos = db.query(Carrinho).order_by(Carrinho.id.desc()).first()
    if not carrinhos:
        return {"itens":[], "total": 0}
    
    itens = []
    total = 0
    
    for item in carrinhos.itens:
        produto = db.query(Produto).filter(Produto.id == item.produto_id).first()
        if not produto:
            continue
        subtotal = produto.Preco * item.quantidade
        total += subtotal
        itens.append({
            "Nome":produto.Nome,
            "Quantidade":item.quantidade,
            "Preco":produto.Preco,
            "Subtotal": subtotal
        })


    return {"itens":itens,
            "total":total}

@RotaCarrinho.delete("/")
async def DeletarProduto( db : Session = Depends(SessionCommerce)):
    carrinho = db.query(Carrinho).order_by(Carrinho.id.desc()).first()
    if not carrinho:
        return {"Mensagem":"Carrinho Vazio"}
    
    db.delete(carrinho)
    db.commit()

    return {"Mensagem":"Carrinho Removido com Sucesso"}