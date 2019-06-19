from bin.hora import get_carga_hr


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