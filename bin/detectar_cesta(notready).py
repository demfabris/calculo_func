def detect_cesta(t):
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