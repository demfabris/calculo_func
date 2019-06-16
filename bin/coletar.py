from bin.scan_escala import *
from bin.hora import transform_hora as transf_hora
from bin.feriados import *


def coletar_nome(STRING_suja):
    t = STRING_suja.split('Funcionário')
    t = t[1]
    t = t.split('Admissão')
    t = t[0]
    t = t.split('-')
    t = t[0]
    return t


def coletar_dias(STRING_limpa):
    aux = STRING_limpa.split('AssinaturadaChefia')
    hora = aux[0].split('TrabalhadaNormal')
    hora = hora[1]
    hora = transf_hora(hora)
    if scan_escala(STRING_limpa) == 1:
        a = round(hora / 11 + feriados_trab(STRING_limpa), 0)
        return int(a)
    elif scan_escala(STRING_limpa) == 2:
        a = round(hora / 7.33 + feriados_trab(STRING_limpa), 0)
        return int(a)
    elif scan_escala(STRING_limpa) == 3:
        a = round(hora / 4.75 + feriados_trab(STRING_limpa), 0)
        return int(a)
    elif scan_escala(STRING_limpa) == 4:
        a = round(hora / 8 + feriados_trab(STRING_limpa), 0)
        return int(a)
    elif scan_escala(STRING_limpa) == 5:
        a = round(hora / 6 + feriados_trab(STRING_limpa), 0)
        return int(a)
    return 0


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