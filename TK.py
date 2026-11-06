import tkinter as tk
import customtkinter as ctk

janela = tk.Tk()
janela.title("Exemplo de Combobox")
janela.geometry("1920x1080")
janela.configure(bg="white")

imagem = tk.PhotoImage(file="img/Logo.png")
logo = tk.Label(janela, image=imagem, bg="white")
logo.place(relx=0.5, rely=0.236, anchor="center")

campo_email = ctk.CTkEntry(
    janela,
    width=677,
    height=98,
    font=("Arial", 20),
    corner_radius=30,
    fg_color="#EEEBEB",
    text_color="#937D7D",
    border_width=0,
    placeholder_text="e-mail"
)

campo_email.place(
    relx=0.5,
    rely=0.465,
    anchor="center"
)

janela.mainloop()