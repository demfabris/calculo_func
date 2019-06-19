from bin.hora import transform_hora as th


def scan_escala(t):
    aux = t.split('Horário')
    if len(aux) > 2:
        return 0
    aux = aux[1]
    aux = aux.split('Funcionário')
    aux = aux[0]
    aux = list(aux)
    if len(aux) < 15:
        return 0
    h1 = aux[:5]
    h2 = aux[15:]
    h1 = ''.join(h1)
    h2 = ''.join(h2)
    result = abs(th(h1) - th(h2))
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
