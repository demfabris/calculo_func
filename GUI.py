# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def runf():
    try:
        execfile('calcfunc.py')
    except FileNotFoundError:
        messagebox.showerror('Erro', 'relatorio.txt não encontrado!')
    else:
        messagebox.showinfo("Ok", 'saida.xlsx gerado com sucesso.')
    finally:
        print(v)


def read_me():
    messagebox.showinfo("LEIA-ME",
    """1) Acesse o site do veltiponto\n2) Vá na aba Relatórios > Ponto > Folha ponto\n3) Insira o período e marque somente funcionários ativos\n4) Vá para aba "Específico", desmarque a caixa de mensagem padrão e escreva exatamente 'endfunc'\n5) Desmarque todas as exibições e deixe somente a de "Trabalho Normal"\n6) Baixe o relatório como .txt e salve na pasta do programa
    
    > Rode
    """)

root = Tk()
root.title("Calcular dias trabalhados")

lb1 = ttk.Label(root, text="""Bem-vindo ao programa cálculo funcionário.\nFavor ler as instruções para evitar erros..""").grid(row=0, column=0, ipady=19)
btn1 = ttk.Button(root, text="Rodar", command=runf).grid(row=3, column=0, sticky=E)
btn2 = ttk.Button(root, text="LEIA-ME", command=read_me).grid(row=0, column=1, padx=15)
btn3 = ttk.Button(root, text="Sair", command=root.quit).grid(row=3, column=1, sticky=W)
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()

positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

root.geometry("+{}+{}".format(positionRight, positionDown))

root.mainloop()
