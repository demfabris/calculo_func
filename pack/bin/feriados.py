def feriados_trab(STRING_limpa):
    count = 0
    if 'Feriado' in STRING_limpa:
        aux = STRING_limpa.split('Feriado')
        for i in range(len(aux)-1):
            vet = aux[i][::-1]
            vet = vet.split('-')
            vet = vet[0]
            vet = list(vet)
            if len(vet) > 10:
                count += 1
    return count
