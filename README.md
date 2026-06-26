import tkinter as tk
from PIL import Image, ImageTk

janela = tk.Tk()
janela.title('Aula para Adicionar Imagem !')
janela.geometry('500x500')

try:
    imagem_original = Image.open("C:/Users/aluno/Downloads/illustration imagem.png")
    imagem_redimensionada = imagem_original.resize((300,300))
    imagem_tkinter = ImageTk.PhotoImage(imagem_redimensionada)

    #Criando um rótulo (Label) para exibir a imagem.

    rotulo_imagem = tk.Label(janela, image=imagem_tkinter)
    rotulo_imagem.pack(pady=20)

except FileNotFoundError:
    aviso_erro = tk.Label(janela, text="Erro: caminho da imagem não encontrado ! \nVerifique o nome do arquivo", fg="red")
