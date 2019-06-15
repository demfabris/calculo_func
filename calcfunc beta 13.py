## -*- coding: utf-8 -*-

#Dependencies: numpy, pandas, python-xlsx,

import time
import pandas as pd
import os

print(
"""%%%%%%%%%%%%%%%%%%%%%%%%%
    %                                                                                   %
    %    CALCULANDO DIAS TRABALHADOS...  %
    %                                                                                   %
    %                                                                                   %
    %%%%%%%%%%%%%%%%%%%%%%%%%
""")

time.sleep(2)

try:
    f = open("relatorio.txt", 'r+', encoding='utf-8')
except FileNotFoundError:
    print("Não encontrei o arquivo relatorio.txt, verifique se ele está na mesma pasta que eu..\n")
    exit()

############################################################


#dividir folha limpa
f.seek(0)
STRING = f.read()
STRING = STRING.split('endfunc')
DADOS_limpo=[]
for aux in STRING:
    aux1 = aux.replace(' ','')
    aux1 = aux1.replace('\n','')
    DADOS_limpo.append(aux1)

#dividir folha suja
DADOS_sujo = []
for aux2 in STRING:
    DADOS_sujo.append(aux2)

DADOS_sujo.pop()
DADOS_limpo.pop()

def scan_escala(t):                                                                             ###Função que trata cada string folha de ponto
    aux=t.split('Horário')                                                                       ###Retorna 1 se for 12/36
    if len(aux) > 2:
        return 0                                                                                       ###Retorna 0 caso o funcionario nao tenha escala
    aux=aux[1]                                                                                      ###Retorna 2 se for diário 07:20
    aux=aux.split('Funcionário')                                                              ###Retorna 3 se for 5h
    aux=aux[0]                                                                                      ###Retorna 4 se for 8h
    aux = list(aux)                                                                                 ###Retorna 5 se for 6h
    if len(aux) < 15:
        return 0
    h1 = aux[:5]
    h2 = aux[15:]
    h1 = ''.join(h1)
    h2 = ''.join(h2)
    result = abs(transf_hora(h1) - transf_hora(h2))
    if result > 11:
        return 1
    elif 8 < result < 10:
        return 2
    elif 4 < result < 6:
        return 3
    elif 10 <= result < 11:                                 ##ARRUMAR
        return 4
    elif result == 6:                                           ##ARRUMAR
        return 5

#######################################################

def coletar_posto(t):
    if 'FORGERINI E INOUYE' in t:
        return 1
    elif 'INOUYE E FORGERINI' in t:
        return 2
    elif 'CRUZEIRO' in t:
        return 3
    elif 'BORBA GATO' in t:
        return 6
    elif 'FENIX' in t:
        return 7
    elif 'REYSSOL' in t:
        return 9

######################################################

def detect_troca(d):
    flag = 0                                                                                                                ##detectar troca de horario no meio da folha
    STR1 = {}
    aux = d.split('Ocorrências')
    aux = aux[1]
    aux = aux.split('Geral')
    aux = aux[0]
    aux = list(aux)
    is_util = lambda x: True if x.isdigit() or x == ':' or x == '-' else False
    vet = ''.join(list(filter( is_util, aux)))
    vet = vet.split('-')
    vet = list(filter( lambda x: x != '', vet))
    for dia in vet:
        STR1[get_carga_hr(dia)] = 0
    for dia in vet:
        STR1[get_carga_hr(dia)] += 1
    result = list(STR1.values())
    result.sort()
    if len(result) > 1:
        flag += 1
        if result[0] > 2:
            flag += 1
    return '*' * flag


#############################################################


def get_carga_hr(s):
    hora=[]
    s = list(s)
    if len(s) == 35:
        hora = s[30:35]
        hora = ''.join(hora)
    return hora


#######################################################

def transf_hora(h):
    if 'Geral' in h:
        h = h.replace('Geral', '')
    elif 'Crédito' in h:
        h = h.replace('Crédito', '')
    aux = h.split(':')
    if aux[0] == '00':
         aux[0] = '24'
    aux[1] =  (int(aux[1]) * 5)/3
    aux[1] = int(round(aux[1],0))
    result = aux[0] + '.' + str(aux[1])
    return float(result)

#######################################################


def coletar_nome(STRING_suja):
    t = STRING_suja.split('Funcionário')
    t = t[1]
    t = t.split('Admissão')
    t = t[0]
    t = t.split('-')
    t = t[0]
    return t

#######################################################

def feriados_trab(STRING_limpa):
    count = 0
    if 'Feriado' in STRING_limpa:
        aux = STRING_limpa.split('Feriado')
        for i in range(len(aux)-1):
            vet = aux[i][::-1]
            vet = vet.split('-')
            vet = vet[0]
            vet = list(vet)
            if len(vet) > 10:
                count += 1
    return count


#######################################################


def coletar_dias(STRING_limpa):
    aux = STRING_limpa.split('AssinaturadaChefia')
    hora = aux[0].split('TrabalhadaNormal')
    hora = hora[1]
    hora = transf_hora(hora)
    if scan_escala(STRING_limpa) == 1:
        a = round((hora) / 11 + feriados_trab(STRING_limpa), 0)
        return int(a)
    elif scan_escala(STRING_limpa) == 2:
        a = round((hora) / 7.33 + feriados_trab(STRING_limpa), 0)
        return int(a)
    elif scan_escala(STRING_limpa) == 3:
        a = round((hora) / 4.75 + feriados_trab(STRING_limpa), 0)
        return int(a)
    elif scan_escala(STRING_limpa) == 4:
        a = round((hora) / 8 + feriados_trab(STRING_limpa), 0)
        return int(a)
    elif scan_escala(STRING_limpa) == 5:
        a = round((hora) / 6 + feriados_trab(STRING_limpa), 0)
        return int(a)
    return 0


####################################################

f.seek(0)
VET = {}
for i, j in zip(DADOS_sujo, DADOS_limpo):
    #F = str(detect_troca(j))
    if coletar_dias(j) <= 0:
        VET.update({str(coletar_nome(i)) + '!': (coletar_dias(j), coletar_posto(i))})
    else:
        VET.update({str(coletar_nome(i) + '*'): (coletar_dias(j), coletar_posto(i))})
STR = pd.DataFrame.from_dict(VET, orient='index', columns=('DIAS', 'POSTO'))
STR.sort_values('POSTO', inplace=True)
STR.to_excel('saida.xlsx')



print('ARQUIVO SAIDA GERADO!\n\nsaindo..')
time.sleep(2)
#os.system('start saida.xlsx')
#exit()


## ARRUMAR FUNC. COM HORARIOS 8 E 6 HORAS