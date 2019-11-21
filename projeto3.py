from tkinter import *
from tkinter import ttk
from functools import partial
from funcoes import *

"""Observação: A função bt_nao está no programa principal para poder fechar a janela_registro,
pois ao colocar essa função no arquivo funcoes.py percebi que a janela não era fechada como eu havia projetado!"""

janela_registro = Tk()

def bt_nao():
    """Função para caso o usuário confirme que não realizou cadastro anteriormente no sistema!"""
    janela_registro.destroy()
    janela_cadastro = Tk()

    def cadastrarLogin():
        """Função para cadastrar um usuário no sistema!"""
        login = usuario1.get()
        senha = primeira.get()
        nivelAcesso = nA.get()      
        arq = open("usuários.txt", "a")
        arq.write(login)
        arq.write("\n")
        arq.write(senha)
        arq.write("\n")
        arq.write(nivelAcesso)
        arq.write("\n")
        arq.close()
        contas = lerArquivo()

    def verificaCadastro():
        """Função para verificar o cadastro realizado pelo usuário!"""
        senha1 = primeira.get()
        senha2 = segunda.get()
        lg = usuario1.get()
        
        if (senha1 == senha2):
            cadastrarLogin()
            janela_cadastro.destroy()
            sucesso = Tk()
            Label(sucesso, text = "Cadastrado com sucesso!").grid(row = 0, column = 0)
            btSucesso = ttk.Button(sucesso, text = "Continuar", command = bt_sim)
            btSucesso.grid(row = 1, column = 0)

            log(lg, "Cadastrou-se")
            sucesso.geometry("140x50+525+150")
            sucesso.mainloop()


        else:
            lab["text"] = "Senhas diferentes!"
            lab["bg"] = "red"



    janela_cadastro.title("Cadastro no sistema")
    Label(janela_cadastro, text = "Login:").grid(row = 0, column = 0)
    Label(janela_cadastro, text = "Senha:").grid(row = 1, column = 0)
    Label(janela_cadastro, text = "Repita sua senha:").grid(row = 2, column = 0)
    Label(janela_cadastro, text = "Nível de Acesso (1 = gerente, 2 = cliente):").grid(row = 3, column = 0)
    lab = Label(janela_cadastro, text = "")
    lab.grid(row = 5, column = 1)
    usuario1 = Entry(janela_cadastro)
    usuario1.grid(row = 0, column = 1)
    primeira = Entry(janela_cadastro, show = "*")
    primeira.grid(row = 1, column = 1)
    segunda = Entry(janela_cadastro, show = "*")
    segunda.grid(row = 2, column = 1)
    nA = Entry(janela_cadastro)
    nA.grid(row = 3, column = 1)

    btCadastro = ttk.Button(janela_cadastro, text = "Cadastrar", command = verificaCadastro) 
    btCadastro.grid(row = 4, column = 1)

    janela_cadastro.geometry("355x140+525+150")
    janela_cadastro.mainloop()


janela_registro.title("Cadastro no sistema")

lb_registro = Label(janela_registro, text = "Você já fez cadastro no sistema?")
lb_registro.grid(row = 0, column = 0, pady = 4)

bt_s = ttk.Button(janela_registro, text = "Sim", width = 11, command = bt_sim)
bt_s.place(x = 10, y = 25)


bt_nao = ttk.Button(janela_registro, text = "Não", width = 11, command = bt_nao)
bt_nao.place(x = 90, y = 25)


janela_registro.geometry("175x60+525+150")
janela_registro.mainloop()