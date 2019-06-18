# -*- coding: utf-8 -*-

import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from bin.coletar import *
from bin.detect_troca import *


def pegar_valor():
    with open("temp.txt", "w+", encoding='utf-8') as file:
        file.write(e1.get())
    main.destroy()


main = Tk()
main.title("Valor diário")
lb1 = ttk.Label(main, text="Valor diário do vale: ").grid(column=0, pady=15)
e1 = Entry(main)
e1.grid(column=1, row=0,padx=10)
btn1 = ttk.Button(main, text="Ok",command=pegar_valor).grid(row=1, column=0, ipadx=10,padx=35, sticky=E)

windowWidth = main.winfo_reqwidth()
windowHeight = main.winfo_reqheight()

positionRight = int(main.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(main.winfo_screenheight() / 2 - windowHeight / 2)

main.geometry("+{}+{}".format(positionRight, positionDown))

main.mainloop()



try:
    f = open("relatorio.txt", 'r+', encoding='utf-8')
except FileNotFoundError:
    messagebox.showerror("Erro","Não encontrei o arquivo relatorio.txt, verifique se ele está na mesma pasta que eu..")
    exit()

f.seek(0)
STRING = f.read()
STRING = STRING.split('endfunc')
DADOS_limpo = []
for aux in STRING:
    aux1 = aux.replace(' ','')
    aux1 = aux1.replace('\n','')
    DADOS_limpo.append(aux1)

DADOS_sujo = []
for aux2 in STRING:
    DADOS_sujo.append(aux2)

DADOS_sujo.pop()
DADOS_limpo.pop()

with open('temp.txt','r+') as file:
    v = file.read()
    v = int(v)

f.seek(0)
VET = {}
for i, j in zip(DADOS_sujo, DADOS_limpo):
    if scan_escala(j) == 1 and coletar_dias(j) > 14:
        VET.update({str(coletar_nome(i)) + detect_troca(j): (coletar_dias(j), coletar_posto(i), (coletar_dias(j)+5)*v)})
    else:
        VET.update({str(coletar_nome(i)) + detect_troca(j): (coletar_dias(j), coletar_posto(i), coletar_dias(j)*v)})
STR = pd.DataFrame.from_dict(VET, orient='index', columns=('DIAS', 'POSTO', 'VALOR'))
STR.sort_values('POSTO', inplace=True)
STR.to_excel('saida.xlsx')

