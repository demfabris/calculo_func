# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def depen():
    try:
        import resources.dependencies
    except FileNotFoundError:
        messagebox.showerror('Erro', 'Dependências não encontradas na pasta raiz.')

def runf():
    try:
        import calcfunc
    except FileNotFoundError or ModuleNotFoundError:
        messagebox.showerror('Erro', 'calcfunc.py não encontrado ou dependências não instaladas')


def read_me():
    messagebox.showinfo("LEIA-ME",
    """1) Acesse o site do VeltiPonto\n\n2) Vá na aba Relatórios > Ponto > Folha ponto\n\n3) Insira o período e marque somente funcionários ativos\n\n4) Vá para aba "Específico", desmarque a caixa de mensagem padrão e escreva exatamente 'endfunc'\n\n5) Desmarque todas as exibições das duas listas e deixe somente a de "Trabalho Normal" e "Falta" na lista da direita\n\n6) Baixe o relatório como .pdf e salve com o nome relatorio.pdf dentro da pasta do programa
    
> Rode
    """)

root = Tk()
root.title("Calcular dias trabalhados")
#root.iconbitmap('icone.ico')
lb1 = ttk.Label(root, text="""Bem-vindo ao programa cálculo funcionário.\nFavor ler as instruções para evitar erros..""").grid(row=0, column=0, ipady=5, padx=10, sticky=E)
lb2= ttk.Label(root, text="Se estiver rodando pela primeira\n vez instale as dependências: ").grid(row=2, column=0)
btn1 = ttk.Button(root, text="Rodar", command=runf).grid(row=3, column=0, pady=15,ipadx=35)
btn2 = ttk.Button(root, text="LEIA-ME", command=read_me).grid(row=0, column=1, padx=15)
btn3 = ttk.Button(root, text="Sair", command=root.destroy).grid(row=3, column=1,padx=35)
btn4 = ttk.Button(root, text="Dependências", command=depen).grid(row=2, column=1, sticky=N)
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()

positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

root.geometry("+{}+{}".format(positionRight, positionDown))

root.mainloop()
