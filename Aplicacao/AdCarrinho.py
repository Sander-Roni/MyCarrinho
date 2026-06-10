import requests 
class MeusItens:
    def __init__(self, produtos, quantidades):
        self.produto = produtos
        self.quantidades = quantidades

    def enviar_dados(self):
        dados = {
            "itens":[{
                "produto_id": self.produto["id"],
                "quantidade":self.quantidades
            }]
        }

        response = requests.post("http://127.0.0.1:8000/Carrinho/",json=dados)
        print(response.status_code)
        print(response.text)

    def consultar_dados(self):
        ''' Conversa Json para Receber Dados'''
        response = requests.get("http://127.0.0.1:8000/Carrinho/")
        dados = response.json()
        dados = dados.get("itens",[])
        print("Debug",dados)

        for i in dados:
            if not isinstance(i, dict):
                print("Item invalido:", i)
                continue 
            valores = (
                f"Produto: {i["Nome"]}\n"
                f"Quantidade: {i["Quantidade"]}\n"
                f"Preco: {i["Preco"]}\n"
                f"Subtotal: {i["Subtotal"]}\n" 
            )
    @staticmethod
    def requisicao_delete():
        response = requests.delete("http://127.0.0.1:8000/Carrinho/")
        print(response)
        dados = response.json()
        print(dados["Mensagem"])

