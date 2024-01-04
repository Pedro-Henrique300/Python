import tkinter
import customtkinter as ctk
from tkinter import *


janela = ctk.CTk()
janela.resizable(False, False)
janela.geometry('600x400')
janela.config(bg='#000')
janela.title('TELA DE LOGIN')
#----------------------------------------------------------------------------------------------------------------------------------

def janela2():
    janela.destroy
    window = ctk.CTk()
    window.geometry('1920x1080')
    window.mainloop()
#---------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------LABEL (TEXT)-----------------------------------------------------

label_title = ctk.CTkLabel(master=janela, 
                           text='ÁREA DE LOGIN', 
                           width=200,
                           bg_color='#000',
                           text_color='#fff')
                           
label_title.place(relx=0.33, rely=0.1)

#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------COLETAR DADOS DE INPUT-------------------------------------------------

def login():
    login1 = input_usuario.get()
    password = input_password.get()
#-------------------------------------------------------------REGRAS DA APLICAÇÃO-------------------------------------------------
    if login1 == 'Pedro' and password == '123':
        tkinter.messagebox.showinfo('LOGIN REALIZADO', 'Login realizado com sucesso')
        janela.destroy
        return janela2()
    else:
        tkinter.messagebox.showerror('ERRO ENCONTRADO', 'Verifique as credenciais')
#----------------------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------INPUTS DE LOGIN----------------------------------------------------

input_usuario = ctk.CTkEntry(master=janela, 
                            placeholder_text='Digite seu usuário', 
                            placeholder_text_color='#fff', 
                            text_color='#fff', 
                            bg_color='#808080', 
                            fg_color='#A9A9A9', 
                            width=200, 
                            height=30)

input_usuario.place(relx= 0.33, rely=0.3)


input_password = ctk.CTkEntry(master=janela, 
                              placeholder_text='Digite sua senha', 
                              placeholder_text_color='#fff', 
                              text_color='#fff', 
                              bg_color='#808080', 
                              fg_color='#A9A9A9', 
                              width=200, 
                              height=30, 
                              show='*')

input_password.place(relx=0.33, rely=0.45)

#----------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------BOTÕES---------------------------------------------------------

login_button = ctk.CTkButton(master=janela, 
                             width=150, 
                             text='LOGIN', 
                             bg_color='#808080', 
                             hover_color='#A9A9A9', 
                             fg_color ='#808080', 
                             cursor='hand2', 
                             command=login)
login_button.place(relx=0.37, rely=0.6)
#----------------------------------------------------------------------------------------------------------------------------------


janela.mainloop()