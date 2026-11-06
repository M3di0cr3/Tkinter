import tkinter as tk
from tkinter import ttk


# Criando janela principal
janela = tk.Tk()

# Configurando a janela
janela.title("Exemplo de Combobox")
janela.geometry("1920x1080")
janela.configure(bg="white")

# Carregar Imagem
imagem = tk.PhotoImage(file="img/Logo.png")

# Criando componente para a logo
logo = tk.Label(janela, image=imagem, bg="white")

#posicionando a logo
logo.place(relx=0.5, rely=0.167, anchor="center")

janela.mainloop()