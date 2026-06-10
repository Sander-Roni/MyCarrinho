import tkinter as tk
import requests
from PIL import Image, ImageTk
# Pegar do APP_Programas a resposta da busca
class Carrinho:
    def __init__(self):
        self.run = tk.Tk()
        self.run.title("Itens No Carrinho")

        self.ImagemLogo = tk.PhotoImage(r"C:\Users\Anuli\Desktop\RestAPIs\API com IA\Aplicacao\Images\arquivo.ico")
        self.run.iconbitmap(False, self.ImagemLogo)

        self.Tenda = Image.open(r"C:\Users\Anuli\Desktop\RestAPIs\API com IA\Aplicacao\Images\Tenda.png")
        self.RedimensionarTenda = self.Tenda.resize((1000,1000), Image.LANCZOS)
        self.CarregarTenda = ImageTk.PhotoImage(self.RedimensionarTenda)

        self.BaseImage = tk.Label(self.run,image=self.CarregarTenda)
        self.ReturnBox = tk.Listbox(self.BaseImage,width=70, height=16, font=('Arial',10,'bold'), background="#ffbd42",foreground="white")
        self.ReturnBox.place(x=0,y=140)
        self.run.geometry("340x280")
        self.BaseImage.pack()
        self.run.resizable(False,False)
        self.Carregar_Metodos()
        self.run.mainloop()

    def Carregar_Metodos(self):
        self.consultar_dados()
        self.BotaoVoltar()
        self.Deletar()

    def consultar_dados(self):
        '''Conversa Json para Receber dados'''
        response = requests.get("http://127.0.0.1:8000/Carrinho/")
        dados = response.json()
        dados = dados.get("itens",[])
        print("Debug",dados)

        self.ReturnBox.delete(0, tk.END)
        if isinstance(dados, dict):
            dados = dados.get("itens", [])

        for i in dados:

            if not isinstance(i, dict):
                print("Item invalido:", i)
                continue 
            # Aqui eu Passo o Tanto de Quantidade apenas do {Produto} que comprei.
            self.ReturnBox.insert(tk.END, 'Itens no Carrinho')
            self.LbBox = tk.Label(self.BaseImage, text="Itens no Carrinho", background="#ffbd42",foreground="white")
            self.LbBox.place(x=0,y=120)
            self.LbBox1 = tk.Label(self.BaseImage, text="-"*120, background="#ffbd42",foreground="white")
            self.LbBox1.place(x=0,y=140)
            self.ReturnBox.insert(tk.END, f'Produto : {i["Nome"]} ')
            self.ReturnBox.insert(tk.END, f'Quantidade : {i["Quantidade"]} ')
            self.ReturnBox.insert(tk.END, f'Preco : {i["Preco"]} ')
            self.ReturnBox.insert(tk.END, f'Subtotal : {i["Subtotal"]} ')
            self.LbBox2 = tk.Label(self.BaseImage, text="-"*120, background="#ffbd42",foreground="white")
            self.LbBox2.place(x=0,y=225)
        
        print(response.status_code)
        print(dados)

    def BotaoVoltar(self):
        self.sair = tk.Button(self.run, text="Voltar", font=('Arial',8,'bold'), command=lambda:self.FuncaoVoltar())
        self.sair.place(x=280,y=5)

    def Deletar(self):
        self.deletar = tk.Button(self.run,text="x", height=-2, width=2,background="#36c2f0",foreground="white",command=self.Apagar)
        self.deletar.place(x=280,y=245)

    def Apagar(self):
        from AdCarrinho import MeusItens 
        MeusItens.requisicao_delete()
        self.ReturnBox.delete(0,tk.END)

    def FuncaoVoltar(self):
        from BuscaDeProduto import Search
        self.run.destroy()
        return Search()


def main():
    carrinho = Carrinho()

if __name__ == "__main__":
    main()
