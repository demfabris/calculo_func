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

