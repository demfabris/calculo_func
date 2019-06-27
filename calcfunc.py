# -*- coding: utf-8 -*-

import PyPDF2 as pdf
import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from bin.coletar import *
from bin.detect import *
from bin.pagamento import *
import os


def abrir():
    os.system('saida.xlsx')
    quit()


def pegar_valor():
    with open("temp.txt", "w+", encoding='utf-8') as arq:
        arq.write(e1.get())
        arq.write('\n')
        arq.write(tkvar.get())
    main.quit()
    main.destroy()
    return

###


main = Tk()
tkvar = StringVar(main)
choices = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro','Dezembro']
lb2 = ttk.Label(main, text="\tMês :").grid(column=0, row=1, pady=5)
menu = ttk.OptionMenu(main, tkvar, choices[1], *choices).grid(column=1, row=1)
main.title("Valor diário")
lb1 = ttk.Label(main, text="      Valor diário do vale : ").grid(column=0, row=0, pady=5)
e1 = Entry(main)
e1.grid(column=1, row=0,padx=10,pady=10)
btn1 = ttk.Button(main, text="Ok",command=pegar_valor).grid(row=2, column=1, ipadx=10, padx=65, pady=15, sticky=E)
tkvar.set('Janeiro') # set the default option


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
    with open("relatorio.pdf", "rb") as folha:                                              # lendo relatorio e limpando
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

with open('temp.txt', 'r+') as file:
    v1 = file.readline()
    mes = file.readline()
    v1 = int(v1)

for i, j in zip(DADOS_sujo, DADOS_limpo):
    VET.update({str(coletar_nome(i) + detect_troca(j) + detect_atm(j)): (coletar_matricula(j), str(coletar_dias(j)), 'P' + str(coletar_posto(i)), 'R$'+str(pagamento(j, mes)*v1)+',00', detect_cesta(j))})
STR = pd.DataFrame.from_dict(VET, orient='index', columns=('MATRICULA', 'DIAS', 'POSTO', 'VALOR', 'CESTA'))
STR.sort_values('POSTO', inplace=True)
STR.to_excel('saida.xlsx')

suc = Tk()
suc.title('Ok')
lb1 = Label(suc, text="saida.xlsx gerado com sucesso!", padx=30, pady=6).grid(row=0)
lb2 = Label(suc, text="Legenda: \n** : Troca de horário.\n@ : ATM importante.").grid(row=1, column= 0, ipady=10)
btn1 = ttk.Button(suc, text='Abrir', command=abrir).grid(row=0, column=1, padx=5,pady=10)
btn2 = ttk.Button(suc, text='Sair', command=suc.destroy).grid(row=1, column=1, pady=5)
windowWidth = suc.winfo_reqwidth()
windowHeight = suc.winfo_reqheight()
positionRight = int(suc.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(suc.winfo_screenheight() / 2 - windowHeight / 2)
suc.geometry("+{}+{}".format(positionRight, positionDown))
suc.mainloop()





