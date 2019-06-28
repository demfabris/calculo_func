from bin.hora import *


def detect_troca(d):
    flag = 0
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
    vet = list(filter(lambda x: True if len(x) == 39 else False, vet))
    vet = list(map(lambda x: x[4:], vet))
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


def detect_atm(t):
    flag = 0
    if 'ATM' in t:
        aux = t.split('ATM')
        aux.pop()
        aux.pop()
        for i in aux:
            vet = i[::-1]
            vet = vet.split('-')
            vet = vet[0]
            if vet.count(":") > 6:
                flag += 1
    return '@' * flag


def detect_cesta(t):
    flag = 0
    check = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15']
    aux = t.split('Ocorrências')
    aux = aux[1]
    aux = aux.split('Geral')
    aux = aux[0]
    aux = list(aux)
    is_util = lambda x: True if x.isdigit() or x == ':' or x == '-' else False
    vet = ''.join(list(filter(is_util, aux)))
    vet = vet.split('-')
    vet = list(filter(lambda x: x != '', vet))
    vet = list(filter(lambda x: True if len(x) > 20 else False, vet))
    for i in vet:
        if i[:2] in check:
            flag += 1
    if flag > 0:
        return 'Sim'
    else:
        return 'Não'


def falta(STRING_limpa):
    aux = STRING_limpa.split('DébitoFalta')
    aux = aux[1]
    aux = aux.split('AssinaturadaChefia')
    aux = aux[0]
    res = transform_hora(aux)
    return int(res)



