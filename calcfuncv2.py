# -*- coding: utf-8 -*-

import PyPDF2 as pdf
import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from bin.coletarv2 import *
from bin.detect_trocav2 import *
import os
from bin.detect_cesta import *


def abrir():
    os.system('saida.xlsx')
    quit()


def pegar_valor():
    with open("temp.txt", "w+", encoding='utf-8') as arq:
        arq.write(e1.get())

    main.quit()
    main.destroy()
    return

###
main = Tk()
main.title("Valor diário")
lb1 = ttk.Label(main, text="Valor diário do vale : ").grid(column=0, pady=5)
e1 = Entry(main)
e1.grid(column=1, row=0,padx=10)
btn1 = ttk.Button(main, text="Ok",command=pegar_valor).grid(row=1, column=0, ipadx=10, padx=35, pady=15, sticky=E)
windowWidth = main.winfo_reqwidth()
windowHeight = main.winfo_reqheight()
positionRight = int(main.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(main.winfo_screenheight() / 2 - windowHeight / 2)
main.geometry("+{}+{}".format(positionRight, positionDown))
main.mainloop()
###

VET = {}
STRING = ''
try:
    with open("relatorio.pdf", "rb") as folha:
        f = pdf.PdfFileReader(folha)
        for page in range(f.getNumPages()):
            temp_page = f.getPage(page)
            STRING += temp_page.extractText()
        STRING = STRING.split('endfunc')
        DADOS_limpo = []
        for aux in STRING:
            aux1 = aux.replace(' ', '')
            aux1 = aux1.replace('\n', '')
            DADOS_limpo.append(aux1)
        DADOS_sujo = []
        for aux2 in STRING:
            DADOS_sujo.append(aux2)
        DADOS_sujo.pop()
        DADOS_limpo.pop()
except FileNotFoundError:
    messagebox.showerror("Erro","Não encontrei o arquivo relatorio.pdf, verifique se ele está na mesma pasta que eu..")
    exit()

with open('temp.txt','r+') as file:
    v = file.read()
    v = int(v)

for i, j in zip(DADOS_sujo, DADOS_limpo):
    if scan_escala(j) == 1 and coletar_dias(j) > 14:
        VET.update({str(coletar_nome(i)) + detect_troca(j): (coletar_dias(j), coletar_posto(i), 'R$'+str((coletar_dias(j)+5)*v)+',00', detect_cesta(j))})
    else:
        VET.update({str(coletar_nome(i)) + detect_troca(j): (coletar_dias(j), coletar_posto(i), 'R$'+str(coletar_dias(j)*v)+',00', detect_cesta(j))})
STR = pd.DataFrame.from_dict(VET, orient='index', columns=('DIAS', 'POSTO', 'VALOR', 'CESTA'))
STR.sort_values('POSTO', inplace=True)
STR.to_excel('saida.xlsx')












suc = Tk()
suc.title('Ok')
lb1 = Label(suc, text="saida.xlsx gerado com sucesso!", padx=30, pady=10).grid(row=0)
btn1 = ttk.Button(suc, text='Abrir saída.xlsx', command=abrir).grid(row=0, column=1)
btn2 = ttk.Button(suc, text='Sair', command=suc.destroy).grid(row=1, column=1,pady=5)
windowWidth = suc.winfo_reqwidth()
windowHeight = suc.winfo_reqheight()
positionRight = int(suc.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(suc.winfo_screenheight() / 2 - windowHeight / 2)
suc.geometry("+{}+{}".format(positionRight, positionDown))
suc.mainloop()





