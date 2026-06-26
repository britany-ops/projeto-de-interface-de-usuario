import tkinter as tk
from tkinter import ttk, messagebox

# Função para adicionar curso
def adicionar():
    curso = entradaCurso.get()
    categoria = comboCategoria.get()

    if curso == "":
        messagebox.showwarning("Aviso", "Digite o nome do curso.")
        return

    listaCursos.insert(tk.END, f"{categoria} - {curso}")

    entradaCurso.delete(0, tk.END)

    messagebox.showinfo("Sucesso", "Curso cadastrado!")

# Função para remover curso
def remover():
    try:
        indice = listaCursos.curselection()[0]
        listaCursos.delete(indice)
        messagebox.showinfo("Removido", "Curso removido!")
    except:
        messagebox.showwarning("Aviso", "Selecione um curso.")

# Função para limpar lista
def limpar():
    listaCursos.delete(0, tk.END)

# Janela
janela = tk.Tk()
janela.title("Cadastro de Cursos")
janela.geometry("450x400")
janela.resizable(False, False)

# Título
titulo = tk.Label(
    janela,
    text="Cadastro de Cursos",
    font=("Arial",16,"bold")
)
titulo.pack(pady=10)

# Categoria
labelCategoria = tk.Label(janela, text="Categoria:")
labelCategoria.pack()

comboCategoria = ttk.Combobox(
    janela,
    values=[
        "Informática",
        "Administração",
        "Saúde",
        "Idiomas",
        "Engenharia"
    ],
    state="readonly"
)

comboCategoria.current(0)
comboCategoria.pack(pady=5)

# Curso
labelCurso = tk.Label(janela, text="Nome do Curso:")
labelCurso.pack()

entradaCurso = tk.Entry(janela, width=40)
entradaCurso.pack(pady=5)

# Botões
btnAdicionar = tk.Button(
    janela,
    text="Adicionar Curso",
    command=adicionar,
    bg="green",
    fg="white",
    width=20
)

btnAdicionar.pack(pady=5)

btnRemover = tk.Button(
    janela,
    text="Remover Curso",
    command=remover,
    bg="red",
    fg="white",
    width=20
)

btnRemover.pack(pady=5)

btnLimpar = tk.Button(
    janela,
    text="Limpar Lista",
    command=limpar,
    bg="gray",
    fg="white",
    width=20
)

btnLimpar.pack(pady=5)

# Listbox
listaCursos = tk.Listbox(
    janela,
    width=50,
    height=10
)

listaCursos.pack(pady=10)

janela.mainloop()
