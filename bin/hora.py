# -*- coding: utf-8 -*-


def get_carga_hr(s):
    hora = []
    s = list(s)
    if len(s) == 35:
        hora = s[30:35]
        hora = ''.join(hora)
    return hora


def transform_hora(h):
    if 'Geral' in h:
        h = h.replace('Geral', '')
    elif 'Crédito' in h:
        h = h.replace('Crédito', '')
    aux = h.split(':')
    #if aux[0] == '00':
        #aux[0] = '24'
    aux[1] = (int(aux[1]) * 5) / 3
    aux[1] = int(round(aux[1], 0))
    result = aux[0] + '.' + str(aux[1])
    return float(result)
