import tkinter as tk 
from PIL import Image, ImageTk
import requests
from AdCarrinho import MeusItens
''' Sisteminha de Busca na Minha Loja...'''

class Search:
    def __init__(self):

        self.win = tk.Tk()
        self.win.geometry("500x500")
        self.win.title("Buscar Produtos")

        self.reload_icon = tk.PhotoImage(r"C:\Users\Anuli\Desktop\RestAPIs\MyCarrinho\Aplicacao\Images\arquivo.ico")
        self.win.iconbitmap(False, self.reload_icon)

        self.win.resizable(False,False)
        startImage = Image.open(r"C:\Users\Anuli\Desktop\RestAPIs\MyCarrinho\Aplicacao\Images\BackgroundForLoja.webp")
        startImageResize = startImage.resize((600,800), Image.LANCZOS)
        self.chargeSrc = ImageTk.PhotoImage(startImageResize)
        self.LabelWin = tk.Label(self.win,image=self.chargeSrc)
        self.LabelWin.pack()

        self.CallMethods()
        self.win.mainloop()
    
    def CallMethods(self):
        self.Pesquisa()
        self.CarregamentoDeImagem()
        self.PesquisaImagem()
        self.ListagemDeItens()
        self.QuantidadeSpinBoxTkinter()
        self.Carrinho_e_SelecaoProduto()
        

    def Pesquisa(self):
        self.search_ = tk.Entry(self.LabelWin)
        self.search_.place(x=180, y=120)

    def CarregamentoDeImagem(self):
        self.src = Image.open(r"Aplicacao/Images/search_img.jpg")
        self.resize = self.src.resize((25,25), Image.LANCZOS)
        self.image = ImageTk.PhotoImage(self.resize)
    
    def PesquisaImagem(self):
        self.load_shop = tk.Button(self.LabelWin,image=self.image, command=lambda:self.ConversaHTTP1())
        self.load_shop.place(x=320,y=110)
#--------------------------------------------------- BUSCA POR API ----------------------------------------------------------------------------#
    ########## Listbox para pegar informações da Minha API #######

    def ListagemDeItens(self):
        self.ArrayObject = tk.Listbox(self.LabelWin, width=30, height=5)
        self.ArrayObject.place(x=160,y=160)
        self.ArrayObject.delete(0,tk.END)

    def ConversaHTTP1(self):
        ############# Aqui meu Tkinter Conversa com o minha API através da Requisição HTTP ###########
        search = str(self.search_.get())
        response = requests.get("http://127.0.0.1:8000/Produtos/",params = {"NomeProduto":search})        
        produtos = response.json() # Me devolve a resposta em json...
        self.produtos = produtos
        self.ArrayObject.delete(0, tk.END)
        for j in produtos:  # Para o item na minha json...
            values = (f'{j["Nome"]} - R$ {j['Preco']}')            
        self.ArrayObject.insert(tk.END, values)
        print(response.status_code)
        print(response.text)
#-------------------------------------------------------------------------------------------------------------------------------------#
    def ImagemDoCarrinho(self):
        self.Buywebp = Image.open(r"C:\Users\Anuli\Desktop\RestAPIs\MyCarrinho\Aplicacao\Images\Buy.webp")
        self.ImageBuywebp = self.Buywebp.resize((20,20), Image.LANCZOS)
        self.DeclarateImage = ImageTk.PhotoImage(self.ImageBuywebp)
        return self.DeclarateImage

    def Carrinho_e_SelecaoProduto(self):
        self.DeclarateImage = self.ImagemDoCarrinho()
        self.BtnBuy = tk.Button(self.LabelWin, text="Adicionar Produto",command=lambda:self.EnviarDados_AoAdicionarNoCarrinho())
        self.BtnBuy.place(x=160,y=260)
        self.AdictCar = tk.Button(self.LabelWin, image=self.DeclarateImage, command=lambda:self.ConsultarDados())
        self.AdictCar.place(x=310, y=260)

    def QuantidadeSpinBoxTkinter(self):
        self.qtd_itens = tk.Spinbox(self.LabelWin, from_=0, to=100, width=-20, font=("Arial", 10))
        self.qtd_itens.place(x=275,y=260)

    def QuantidadesObtidas(self):
        return int(self.qtd_itens.get())

    def SelecionarItemPor_ID(self):
        selection_product = self.ArrayObject.curselection()
        if not selection_product:
            return None 
        if selection_product:
            index = selection_product[0]
            produto = self.produtos[index]
            return produto

    def EnviarDados_AoAdicionarNoCarrinho(self):
        produto = self.SelecionarItemPor_ID()
        quantidades_obtidas = self.QuantidadesObtidas()
        if produto is None or quantidades_obtidas <= 0:
            return 
        # Chamando minha janela de AdicionarCarrinho
        MeusItens(produto,quantidades_obtidas).enviar_dados()

    def ConsultarDados(self):
        from ItensDoCarrinho import Carrinho
        self.win.destroy()
        Carrinho()

        
    
def main():
    run = Search()

if __name__ == "__main__":
    main()