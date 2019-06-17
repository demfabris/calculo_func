# -*- coding: utf-8 -*-

import calcfunc
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def runf():
    try:
        execfile('calcfunc.py')
    except FileNotFoundError:
        messagebox.showwarning('Erro', 'Relatorio.txt não encontrado!')

root = Tk()
root.title("Calcular dias trabalhados")

lb1 = ttk.Label(root, text="Verifique se o relatorio.txt está na mesma pasta que eu..").pack(side='top')
lb2 = ttk.Label(root, text='Valor diário do vale:').pack(side ='left')
e1 = ttk.Entry(root).pack(side = "left")
btn1 = ttk.Button(root, text="Rodar", command = runf).pack(side = 'right', ipady=10)
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()

positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

root.geometry("+{}+{}".format(positionRight, positionDown))

root.mainloop()