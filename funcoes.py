from tkinter import *
from tkinter import ttk
from functools import partial

def dataHora():
    """Função que coleta a data e hora atual!"""
    from datetime import datetime
    dataHora = datetime.now()
    dataHora = dataHora.strftime("%d/%m/%Y %H:%M")
    return dataHora

def log(nome, acao):
    """Função que armazena em um arquivo .csv as operações realizadas pelo usuário no sistema!"""
    nm = nome
    action = acao
    arq = open("log.csv", "a")
    arq.write(nm)
    arq.write(";")
    arq.write(action)
    arq.write(";")
    arq.write(dataHora())
    arq.write("\n")
    arq.close()

def eliminaBarraEne(string):
    """Função para retirar o \n para melhor leitura do arquivo elementos.txt"""
    stringNova = ""
    for caractere in string:
        if (caractere != "\n"):
            stringNova += caractere
    return stringNova

def lerArquivo():
    """Função para ler o arquivo usuários.txt"""
    contas ={}
    arq = open("usuários.txt", "r")
    linhas = arq.readlines()
    arq.close()
    qtdeLogins = len(linhas) // 3
    cont = 0
    while (cont < qtdeLogins):
        login = eliminaBarraEne(linhas[3*cont])
        senha = eliminaBarraEne(linhas[3*cont+1])
        nivelAcesso = eliminaBarraEne(linhas[3*cont+2])
        usuarios = (login, senha, nivelAcesso)
        contas[2*cont+1] = usuarios
        cont += 1
    return contas

def bt_sim():
    """Função para caso o usuário confirme que já está cadastrado no sistema, permitindo que ele faça login!"""
    janela = Tk()

    def lerArquivo2():
        """Função para ler o arquivo elementos.txt e retornar um dicionário com os produtos cadastrados!"""
        dicionario ={}
        arq = open("elementos.txt", "r")
        linhas = arq.readlines()
        arq.close()
        qtdeProdutos = len(linhas) // 7
        cont = 0
        while (cont < qtdeProdutos):
            nomeProduto = eliminaBarraEne(linhas[7*cont])
            codigoProduto = eliminaBarraEne(linhas[7*cont+1])
            notaFiscal = eliminaBarraEne(linhas[7*cont+2])
            quantidade = eliminaBarraEne(linhas[7*cont+3])
            preco = eliminaBarraEne(linhas[7*cont+4])
            dataHora = eliminaBarraEne(linhas[7*cont+5])
            dataModificacao = eliminaBarraEne(linhas[7*cont+6])
            produtos = (nomeProduto, quantidade, preco, dataHora)
            dicionario[codigoProduto + notaFiscal] = produtos
            cont += 1
        return dicionario
        

    def verificaConta():
        """Função para verificar as credenciais do usuário ao fazer login!"""
        validar = False
        login = ed1.get()
        senha = ed2.get()
        nivelAcesso = ed3.get()
        contas = lerArquivo()
        usuario = contas.keys()
        for chave in usuario:
            if (contas[chave] == (login, senha, nivelAcesso)):
                validar = nivelAcesso
                return validar, login
        return "0"

    def bt_click():
        """Função para chamar a verificação da conta do usuário e entrar no controle de estoque!"""
        validar = verificaConta()
        if (validar != "0"):
            lg = validar[1]
            log(lg, "Entrou no sistema")

        def opcao(botao):
            """Função para verificar qual botão foi apertado pelo usuário no menu principal do sistema!"""
            comando = botao["text"]

            def cadastrarProduto():
                """Função para cadastrar um produto no arquivo elementos.txt"""
                nomeProduto = nome.get()
                codigoProduto = codigo.get()
                notaFiscal = nota.get()
                quantidade = qtde.get()
                preco = price.get()  
                cadastro.destroy()  
                arq = open("elementos.txt", "a")
                arq.write(nomeProduto)
                arq.write("\n")
                arq.write(codigoProduto)
                arq.write("\n")
                arq.write(notaFiscal)
                arq.write("\n")
                arq.write(quantidade)
                arq.write("\n")
                arq.write(preco)
                arq.write("\n")
                arq.write(dataHora())
                arq.write("\n")
                arq.write(dataHora())
                arq.write("\n")
                arq.close()
                produtos = lerArquivo2()
                log(lg, "Cadastrou um produto")

            def removerProduto():
                """Função para remover um produto do arquivo elementos.txt"""
                code_remover = cdProduto.get()
                nota_remover = nf.get()
                chave_remover = code_remover + nota_remover
                remover.destroy()

                arq = open("elementos.txt", "r")
                linhas = arq.readlines()
                arq.close()
                qtdeProdutos = len(linhas) // 7
                arq = open("elementos.txt", "w")
                cont = 0
                arq.close()
                while (cont < qtdeProdutos):
                    nomeProduto = eliminaBarraEne(linhas[7*cont])
                    codigoProduto = eliminaBarraEne(linhas[7*cont+1])
                    notaFiscal = eliminaBarraEne(linhas[7*cont+2])
                    quantidade = eliminaBarraEne(linhas[7*cont+3])
                    preco = eliminaBarraEne(linhas[7*cont+4])
                    dataHora = eliminaBarraEne(linhas[7*cont+5])
                    dataModificacao = eliminaBarraEne(linhas[7*cont+6])
                    identificador = codigoProduto + notaFiscal
                        
                    if (identificador != chave_remover):
                        arq = open("elementos.txt", "a")
                        arq.write(nomeProduto)
                        arq.write("\n")
                        arq.write(codigoProduto)
                        arq.write("\n")
                        arq.write(notaFiscal)
                        arq.write("\n")
                        arq.write(quantidade)
                        arq.write("\n")
                        arq.write(preco)
                        arq.write("\n")
                        arq.write(dataHora)
                        arq.write("\n")
                        arq.write(dataModificacao)
                        arq.write("\n")
                        arq.close()
                    cont += 1
                produtos = lerArquivo2()
                log(lg, "Removeu um produto")

            def buscarProduto():
                """Função para buscar um produto no dicionário que contém as informações do arquivo elementos.txt"""
                codigo_buscar = code.get()
                nota_buscar = cdFiscal.get()
                chave_buscar = codigo_buscar + nota_buscar
                produtos = lerArquivo2()
                key = produtos.keys()

                if (chave_buscar in key):
                    produtoPesquisado = produtos[chave_buscar]
                    nome = produtoPesquisado[0]
                    quantidad = produtoPesquisado[1]
                    prec = produtoPesquisado[2]
                    hour = produtoPesquisado[3]
                    
                    lab["text"] = ("Nome: " + nome) + "\n" + ("Quantidade: " + quantidad) + "\n" + ("Preço: " + prec)  + "\n" + ("Data: " + hour)
                    lab["bg"] = "green"

                else:
                    lab["text"] = "Código de produto ou nota fiscal inválido!"
                    lab["bg"] = "red"

                log(lg, "Buscou um produto")

            def atualizarProduto():
                """Função para atualizar as informações de um produto no arquivo elementos.txt"""
                nome_produto = _nome_.get()
                cd = codigo.get()
                fiscal = nota.get()
                quant = qtde.get()
                pricy = price.get()
                chave_atualizar = cd + fiscal
                janela_att.destroy()

                arq = open("elementos.txt", "r")
                linhas = arq.readlines()
                arq.close()
                qtdeLinhas = len(linhas) // 7
                arq = open("elementos.txt", "w")
                arq.close()
                cont = 0
                while (cont < qtdeLinhas):
                    nomeProduto = eliminaBarraEne(linhas[7*cont])
                    codigoProduto = eliminaBarraEne(linhas[7*cont+1])
                    notaFiscal = eliminaBarraEne(linhas[7*cont+2])
                    quantidade = eliminaBarraEne(linhas[7*cont+3])
                    preco = eliminaBarraEne(linhas[7*cont+4])
                    data = eliminaBarraEne(linhas[7*cont+5])
                    dataModificacao = eliminaBarraEne(linhas[7*cont+6])
                    identificador = codigoProduto + notaFiscal

                    if (identificador != chave_atualizar):
                        arq = open("elementos.txt", "a")
                        arq.write(nomeProduto)
                        arq.write("\n")
                        arq.write(codigoProduto)
                        arq.write("\n")
                        arq.write(notaFiscal)
                        arq.write("\n")
                        arq.write(quantidade)
                        arq.write("\n")
                        arq.write(preco)
                        arq.write("\n")
                        arq.write(data)
                        arq.write("\n")
                        arq.write(dataModificacao)
                        arq.write("\n")
                        arq.close()

                    else:
                        arq = open("elementos.txt", "a")
                        arq.write(nome_produto)
                        arq.write("\n")
                        arq.write(codigoProduto)
                        arq.write("\n")
                        arq.write(notaFiscal)
                        arq.write("\n")
                        arq.write(quant)
                        arq.write("\n")
                        arq.write(pricy)
                        arq.write("\n")
                        arq.write(data)
                        arq.write("\n")
                        arq.write(dataHora())
                        arq.write("\n")
                        arq.close()
                    cont += 1
                log(lg, "Atualizou um produto")
                
                    


            if (comando == "Cadastrar um produto"):
                cadastro = Tk()
                cadastro.title("Cadastro do produto")
                Label(cadastro, text = "Nome do produto:").grid(row = 0, column = 0)
                Label(cadastro, text = "Código do produto:").grid(row = 1, column = 0)
                Label(cadastro, text = "Código da nota fiscal:").grid(row = 2, column = 0)
                Label(cadastro, text = "Quantidade de itens:").grid(row = 3, column = 0)
                Label(cadastro, text = "Preço por unidade:").grid(row = 4, column = 0)

                nome = Entry(cadastro)
                nome.grid(row = 0, column = 1)

                codigo = Entry(cadastro)
                codigo.grid(row = 1, column = 1)

                nota = Entry(cadastro)
                nota.grid(row = 2, column = 1)

                qtde = Entry(cadastro)
                qtde.grid(row = 3, column = 1)

                price = Entry(cadastro)
                price.grid(row = 4, column = 1)

                cadastrar = ttk.Button(cadastro, text = "Cadastrar", command = cadastrarProduto)
                cadastrar.grid(row = 5, column = 1)                    

                cadastro.geometry("250x130+525+150")
                cadastro.mainloop()

            elif (comando == "Remover um produto"):
                remover = Tk()
                remover.title("Remoção de produto")

                Label(remover, text = "Código do produto:").grid(row = 0, column = 0)
                Label(remover, text = "Nota fiscal do produto:").grid(row = 1, column = 0)

                cdProduto = Entry(remover)
                cdProduto.grid(row = 0, column = 1)

                nf = Entry(remover)
                nf.grid(row = 1, column = 1)

                bt_remover = ttk.Button(remover, text = "Remover", command = removerProduto)
                bt_remover.grid(row = 2, column = 1)

                remover.geometry("265x100+525+150")
                remover.mainloop()

            elif (comando == "Buscar um produto"):
                buscar = Tk()
                buscar.title("Busca de produtos")

                lab = Label(buscar, text = "")
                lab.grid(row = 3, column = 1)

                Label(buscar, text = "Código do produto:").grid(row = 0, column = 0)
                Label(buscar, text = "Nota fiscal do produto:").grid(row = 1, column = 0)

                code = Entry(buscar)
                code.grid(row = 0, column = 1)

                cdFiscal = Entry(buscar)
                cdFiscal.grid(row = 1, column = 1)

                bt_buscar = ttk.Button(buscar, text = "Buscar", command = buscarProduto)
                bt_buscar.grid(row = 2, column = 1)

                buscar.geometry("375x150+525+150")
                buscar.mainloop()

            elif (comando == "Gerar relatório"):
                def ordem(lista, listaNova = []):
                    """Função para organizar uma lista em ordem alfabética!"""
                    if (len(lista) == 1):
                        listaNova.append(lista[0])
                        return lista[0]
                        
                    else:
                        alfaOrdem = min(lista)
                        lista.remove(alfaOrdem)
                        listaNova.append(alfaOrdem)
                        return listaNova, ordem(lista)
                
                def relatorio():
                    """Função para gerar um relatório utilizando a função ordem para gerar o relatório de maneira organizada!"""
                    lista = []
                    listaNomes = []
                    arq = open("elementos.txt", "r")
                    linhas = arq.readlines()
                    arq.close()
                    cont = 0
                    cont2 = 0

                    while (cont < len(linhas) // 7):
                        nomeProduct = eliminaBarraEne(linhas[7*cont])
                        listaNomes.append(nomeProduct)
                        cont += 1
                    
                    listaOrdenada = ordem(listaNomes)
                    listaOrdenada2 = listaOrdenada[0]

                    arq = open("relatório.csv", "w")
                    arq.write("Nome do produto;")
                    arq.write("Código do produto;")
                    arq.write("Nota fiscal;")
                    arq.write("Quantidade em estoque;")
                    arq.write("Preço;")
                    arq.write("Data de criação;")
                    arq.write("Data de modificação")
                    arq.write("\n")

                    while(cont2 < len(linhas) // 7):
                        nomeProduto = eliminaBarraEne(linhas[7*cont2])
                        codigoProduto = eliminaBarraEne(linhas[7*cont2+1])
                        notaFiscal = eliminaBarraEne(linhas[7*cont2+2])
                        quantidade = eliminaBarraEne(linhas[7*cont2+3])
                        preco = eliminaBarraEne(linhas[7*cont2+4])
                        dataHora = eliminaBarraEne(linhas[7*cont2+5])
                        dataModificacao = eliminaBarraEne(linhas[7*cont2+6])
                        produto = (nomeProduto, codigoProduto, notaFiscal, quantidade, preco, dataHora, dataModificacao)
                        lista.append(produto)

                        if (len(listaOrdenada2) == 0):
                            return 0

                        elif (listaOrdenada2[0] == nomeProduto):
                            arq = open("relatório.csv", "a")
                            arq.write(nomeProduto)
                            arq.write(";")
                            arq.write(codigoProduto)
                            arq.write(";")
                            arq.write(notaFiscal)
                            arq.write(";")
                            arq.write(quantidade)
                            arq.write(";")
                            arq.write(preco)
                            arq.write(";")
                            arq.write(dataHora)
                            arq.write(";")
                            arq.write(dataModificacao)
                            arq.write("\n")
                            arq.close()
                            listaOrdenada2.remove(listaOrdenada2[0])
                            cont2 = 0
                        cont2 += 1

                relatorio()
                log(lg, "Gerou um relatório")
                        
            elif (comando == "Atualizar informações"):
                janela_att = Tk()
                janela_att.title("Atualizar produto")
                Label(janela_att, text = "Nome do produto:").grid(row = 0, column = 0)
                Label(janela_att, text = "Código do produto:").grid(row = 1, column = 0)
                Label(janela_att, text = "Código da nota fiscal:").grid(row = 2, column = 0)
                Label(janela_att, text = "Quantidade de itens:").grid(row = 3, column = 0)
                Label(janela_att, text = "Preço por unidade:").grid(row = 4, column = 0)

                _nome_ = Entry(janela_att)
                _nome_.grid(row = 0, column = 1)

                codigo = Entry(janela_att)
                codigo.grid(row = 1, column = 1)

                nota = Entry(janela_att)
                nota.grid(row = 2, column = 1)

                qtde = Entry(janela_att)
                qtde.grid(row = 3, column = 1)

                price = Entry(janela_att)
                price.grid(row = 4, column = 1)

                atualizar = ttk.Button(janela_att, text = "Atualizar", command = atualizarProduto)
                atualizar.grid(row = 5, column = 1)                    

                janela_att.geometry("255x140+525+150")
                janela_att.mainloop()

            elif (comando == "Sair"):
                log(lg, "Saiu do sistema")
                janela2.destroy()

            elif (comando == "Sair "):
                log(lg, "Saiu do sistema")
                janela3.destroy()

        if (validar[0] == "1"):
            janela.destroy()
            janela2 = Tk()   

            janela2.title("Controle de estoque")

            Label(janela2, text = "1-").grid(row = 0, column = 0)
            Label(janela2, text = "2-").grid(row = 1, column = 0)
            Label(janela2, text = "3-").grid(row = 2, column = 0)
            Label(janela2, text = "4-").grid(row = 3, column = 0)
            Label(janela2, text = "5-").grid(row = 4, column = 0)
            Label(janela2, text = "6-").grid(row = 5, column = 0)

            opcao1 = ttk.Button(janela2, text = "Cadastrar um produto", width = 20)
            opcao1.grid(row = 0, column = 1)
            opcao1["command"] = partial(opcao, opcao1)

            opcao2 = ttk.Button(janela2, text = "Remover um produto", width = 20)
            opcao2.grid(row = 1, column = 1)
            opcao2["command"] = partial(opcao, opcao2)

            opcao3 = ttk.Button(janela2, text = "Buscar um produto", width = 20)
            opcao3.grid(row = 2, column = 1)
            opcao3["command"] = partial(opcao, opcao3)

            opcao4 = ttk.Button(janela2, text = "Gerar relatório", width = 20)
            opcao4.grid(row = 3, column = 1)
            opcao4["command"] = partial(opcao, opcao4)

            opcao5 = ttk.Button(janela2, text = "Atualizar informações", width = 20)
            opcao5.grid(row = 4, column = 1)
            opcao5["command"] = partial(opcao, opcao5)

            opcao6 = ttk.Button(janela2, text = "Sair", width = 20)
            opcao6.grid(row = 5, column = 1)
            opcao6["command"] = partial(opcao, opcao6)
        

            janela2.geometry("350x345+525+150")
            janela2.mainloop()

        elif (validar[0] == "2"):
            janela3 = Tk()
            janela3.title("Menu")

            Label(janela3, text = "1-").grid(row = 0, column = 0)
            Label(janela3, text = "2-").grid(row = 1, column = 0)
            Label(janela3, text = "3-").grid(row = 2, column = 0)

            op = ttk.Button(janela3, text = "Buscar um produto", width = 20)
            op.grid(row = 0, column = 1)
            op["command"] = partial(opcao, op)
            

            op2 = ttk.Button(janela3, text = "Gerar relatório", width = 20)
            op2.grid(row = 1, column = 1)
            op2["command"] = partial(opcao, op2)
            

            op3 = ttk.Button(janela3, text = "Sair ", width = 20)
            op3.grid(row = 2, column = 1)
            op3["command"] = partial(opcao, op3)
            
            janela3.geometry("275x130+525+150")
            janela3.mainloop()

        else:
            lb["text"] = "Credenciais Inválidas!"
            lb["bg"] = "red"


    janela.title("Login do Sistema")

    login = Label(janela, text = "Login:")
    login.grid(row = 0, column = 0)

    senha = Label(janela, text = "Senha")
    senha.grid(row = 1, column = 0)

    acesso = Label(janela, text = "Nivel de acesso (1 ou 2):")
    acesso.grid(row = 2, column = 0)

    lb = Label(janela, text = "")
    lb.grid(row = 5, column = 1)

    ed1 = Entry(janela)
    ed1.grid(row = 0, column = 1)

    ed2 = Entry(janela, show = "*")
    ed2.grid(row = 1, column = 1)

    ed3 = Entry(janela)
    ed3.grid(row = 2, column = 1)

    bt = ttk.Button(janela, text = "Confirmar", command = bt_click)
    bt.grid(row = 4, column = 1)

    janela.geometry("275x130+525+150")
    janela.mainloop()