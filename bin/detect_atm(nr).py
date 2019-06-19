def detect_atm(t):
    aux = t.split('Ocorrências')
    aux = aux[1]
    aux = aux.split('Geral')
    aux = aux[0]
    if aux.count('ATM') > 1:
        aux = aux.split('ATM')
        aux.pop()
        for i in aux:
            vet = i[::-1]



