from calculo import *
    
cpf_user = int(input('Digite seu CPF: '))
cpf = [int(x) for x in str(cpf_user)] 
*cpf_usavel, digito_1, digito_2 = cpf

print('CPF Válido!') if calculo_digito1(cpf_usavel) == digito_1 and calculo_digito2(cpf_usavel) == digito_2 else print('CPF Inválido!')
