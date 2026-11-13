import tkinter as tk
import customtkinter as ctk 

#----Janela----
janela = ctk.CTk()
janela.geometry("1920x1080")
janela.configure(bg="white")

tela_login = ctk.CTkFrame(janela, fg_color="white")
tela_login.pack(fill="both", expand=True)

tela_principal = ctk.CTkFrame(janela, fg_color="white")

def acessar():
    tela_login.pack_forget()
    tela_principal.pack(fill="both", expand=True)

#----Primeira tela----
imagem = tk.PhotoImage(file="img/Logo.png")
logo = tk.Label(tela_login, image=imagem, bg="white")
logo.place(relx=0.5, rely=0.236, anchor="center")

campo_email = ctk.CTkEntry(
    tela_login,
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

campo_senha = ctk.CTkEntry(
    tela_login,
    width=677,
    height=98,
    font=("Arial", 20),
    corner_radius=30,
    fg_color="#EEEBEB",
    text_color="#937D7D",
    border_width=0,
    placeholder_text="senha",
    show="*"
)
campo_senha.place(
    relx=0.5,
    rely=0.6,
    anchor="center"
)

botao_acessar = ctk.CTkButton(
    tela_login,
    width=677,
    height=98,
    font=("Arial", 20),
    corner_radius=30,
    fg_color="#298FC2",
    text_color="white",
    border_width=0,
    text="Acessar",
    command=acessar
)
botao_acessar.place(
    relx=0.5,
    rely=0.72,
    anchor="center"
)

primeiro_acesso = ctk.CTkLabel(
    tela_login,
    text="Primeiro acesso?",
    font=("Arial", 18),
    text_color="#298FC2"
)
primeiro_acesso.place(
    relx=0.5,
    rely=0.80,
    anchor="center"
)


#----Segunda tela----

imagem_perfil = tk.PhotoImage(file="img/Avatar.png")
perfil = tk.Label(tela_principal, image=imagem_perfil, bg="white", borderwidth=0)
perfil.place(
    x=50,
    y=50,
)

bem_vindo = ctk.CTkLabel(
    tela_principal,
    width=241,
    height=62,
    corner_radius=30,
    border_width=0,
    font=("Arial", 20),
    fg_color="#CAE8F7",
    text_color="#298FC2",
    text="Bem-vindo(a)!"
)
bem_vindo.place(
    x=170,
    y=63,
)

janela.mainloop()
