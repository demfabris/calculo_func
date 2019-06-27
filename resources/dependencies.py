#dependencies.py

import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def install_dep():
    aux = tkvar.get()
    os.system('pip install {}'.format(aux))
    messagebox.showinfo("Ok", "Dependência Instalada.")



src = Tk()
tkvar = StringVar(src)
choices = ['numpy', 'pandas', 'openpyxl', 'PyPDF2', 'pywin32', 'pyexcel-xlsx']
src.title("Dependências. ")
lb1 = ttk.Label(src, text="Instalar dependências: ").grid(row=0,column=0, ipady=15,padx=15)
btn1 = ttk.Button(src, text = 'Instalar', command=install_dep).grid(row=1,column=0,pady=15)
btn1 = ttk.Button(src, text = 'Sair', command=src.destroy).grid(row=1, column=1)
menu = ttk.OptionMenu(src, tkvar, choices[1], *choices).grid(row=0, column=1, padx=10)
tkvar.set('numpy')

windowWidth = src.winfo_reqwidth()
windowHeight = src.winfo_reqheight()
positionRight = int(src.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(src.winfo_screenheight() / 2 - windowHeight / 2)
src.geometry("+{}+{}".format(positionRight, positionDown))
src.mainloop()