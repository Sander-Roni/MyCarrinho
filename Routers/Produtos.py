from Models.EcommerceModel import Produto,LoteProduto
from Schemas.EcommerceSchema import ProdutoSchema
from dependencies import SessionCommerce
from fastapi import APIRouter, Depends, HTTPException

RouterProducts = APIRouter(prefix="/Produtos",tags=["produtos da loja"])

@RouterProducts.post("/")
async def CadastrarProdutos(schema_produto : ProdutoSchema, SessionProdutos = Depends(SessionCommerce)):
    ''' Cadastro de Produtos'''
    produtos = SessionProdutos.query(Produto).filter(Produto.Nome  == schema_produto.Nome).first()

    if produtos:
        raise HTTPException(status_code = 404, detail="O produto já existe")
    
    novo_produto = Produto(
        Nome = schema_produto.Nome,
        Ean = schema_produto.Ean,
        Preco = schema_produto.Preco,
        Estoque = schema_produto.Estoque
    )

    SessionProdutos.add(novo_produto)
    SessionProdutos.commit()


@RouterProducts.get("/")
async def BuscarProduto(NomeProduto: str, SessionProdutos = Depends(SessionCommerce)):
    ''' Consulta de Produtos'''
    produtos = SessionProdutos.query(Produto).filter(Produto.Nome.contains(NomeProduto)).all()

    return produtos

@RouterProducts.put("/")
async def AtualizarProdutos(sessionproduto : int, SchemaProdutos : ProdutoSchema,SessionProdutos = Depends(SessionCommerce)):
    ''' Atualização de Produtos'''
    produtos = SessionProdutos.query(Produto).filter(Produto.id == sessionproduto).first()

    if not produtos:
        raise HTTPException(status_code = 404, detail="O Item não pode ser encontrado para Atualização...")
    
    produtos.Nome = SchemaProdutos.Nome
    produtos.Ean = SchemaProdutos.Ean
    produtos.Preco = SchemaProdutos.Preco 
    produtos.Estoque = SchemaProdutos.Estoque 
    SessionProdutos.commit()

    return {"Mensagem":"Produtos atualizados na Loja Com Sucesso!"}
        
@RouterProducts.delete("/")
async def DeletarProdutos(sessionproduto : int, SessionProdutos = Depends(SessionCommerce)):
    ''' Deletar produtos da Plataforma'''
    produtos = SessionProdutos.query(Produto).filter(Produto.id == sessionproduto).first()
    if not produtos:
        raise HTTPException(status_code=404, detail="Não foi possivel encontrar o Produto para a Exclusão")

    SessionProdutos.delete(produtos)
    SessionProdutos.commit()

    return {"Mensagem":"Produto excluido com sucesso!"}