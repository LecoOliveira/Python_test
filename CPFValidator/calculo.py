
def calculo_digito1(cpf_usavel):

    contador = 10
    numeros_multiplicados = []

    for num in cpf_usavel:
        multiplica = num * contador
        contador -= 1
        numeros_multiplicados.append(multiplica)

    soma_cpf_usavel = sum(numeros_multiplicados)

    calculo = 11 - (soma_cpf_usavel % 11)
    digito_final_1 = 0 if calculo > 9 else calculo

    return digito_final_1


def calculo_digito2(cpf_usavel):

    cpf_usavel.append(calculo_digito1(cpf_usavel))
    contador = 11
    numeros_multiplicados = []

    for num in cpf_usavel:
        multiplica = num * contador
        contador -= 1
        numeros_multiplicados.append(multiplica)

    soma_cpf_usavel = sum(numeros_multiplicados)

    calculo = 11 - (soma_cpf_usavel % 11)
    cpf_usavel.pop()
    return calculo