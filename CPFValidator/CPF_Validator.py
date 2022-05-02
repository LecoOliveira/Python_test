
def calculo_digito1():

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


def calculo_digito2():

    cpf_usavel.append(calculo_digito1())
    contador = 11
    numeros_multiplicados = []

    for num in cpf_usavel:
        multiplica = num * contador
        contador -= 1
        numeros_multiplicados.append(multiplica)

    soma_cpf_usavel = sum(numeros_multiplicados)

    calculo = 11 - (soma_cpf_usavel % 11)
    return calculo


if __name__ == '__main__':
    
    cpf_user = int(input('Digite seu CPF: '))
    cpf = [int(x) for x in str(cpf_user)] 
    *cpf_usavel, digito_1, digito_2 = cpf

    print('CPF Válido!') if calculo_digito1() == digito_1 and calculo_digito2() == digito_2 else print('CPF Inválido!')
