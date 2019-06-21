# -*- coding: utf-8 -*-

def detect_atm_nr(t):
    flag = 0
    aux = t.split('Ocorrências')
    aux = aux[1]
    aux = aux.split('Geral')
    aux = aux[0]
    if aux.count('ATM') > 1:
        aux = aux.split('ATM')
        aux.pop()
        aux.pop()
        for i in aux:
            vet = i[::-1]
            if vet.count(":") > 6:
                flag+=1
    return '@' * flag

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


