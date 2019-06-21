from bin.scan_escalav2 import *
from bin.feriados import *
from bin.hora import transform_hora as transf_hora


def coletar_nome(STRING_suja):
    aux = STRING_suja
    comp = ['05.654.707/0001-35', '44.955.474/0001-62', '67.379.743/0001-95', '09.561.664/0001-02', '00.218.960/0001-22', '02.845.415/0001-91','67.379.743/0002-76']
    for i in comp:
        if i in STRING_suja:
            aux = aux.split(i)
            aux = aux[1]
            aux = aux.split('-')
            aux = aux[0]
            aux = list(filter(lambda x: False if x.isdigit() or x == '/' else True, aux))
            aux = ''.join(aux)
    return aux


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


def coletar_posto(STRING_suja):
    if '67.379.743/0001-95' in STRING_suja:
        return 1
    elif '44.955.474/0001-62' in STRING_suja:
        return 2
    elif '02.845.415/0001-91' in STRING_suja:
        return 3
    elif '09.561.664/0001-02' in STRING_suja:
        return 6
    elif '05.654.707/0001-35' in STRING_suja:
        return 7
    elif '67.379.743/0002-76' in STRING_suja:
        return 8
    elif '00.218.960/0001-22' in STRING_suja:
        return 9
    else:
        return 99


def coletar_matricula(STRING_limpa):
    aux = STRING_limpa.split('Funcionário')
    aux = aux[0]
    aux = aux.split('-')
    aux = aux.pop()
    return str(aux)