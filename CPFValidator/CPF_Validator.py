from calculo import *

tentativa = 3

while True:
   
    try:
        cpf_user = int(input('Digite seu CPF: '))
        cpf = [int(x) for x in str(cpf_user)] 
        *cpf_usavel, digito_1, digito_2 = cpf
        digitos =  [calculo_digito1(cpf_usavel), calculo_digito2(cpf_usavel)]
        cpf_usavel.pop()
        cpf_novo = cpf_usavel + digitos
        sequencia = ''.join(map(str, cpf_novo)) == str(cpf_novo[0]) * 11

        print('CPF Válido!') if cpf_novo == cpf and not sequencia else print('CPF Inválido!')
        
        break
    
    except Exception as erro:
        print(f'Erro: {erro}\n')
        tentativa -= 1
        if tentativa == 0:
            print('Tentativas excedidas. Inicie o programa novamente.')
            break
        else:
            continue

    except KeyboardInterrupt:
        print('\nFim do programa. \nObrigado!')
        break