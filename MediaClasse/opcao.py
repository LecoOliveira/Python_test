# -*- coding: utf-8 -*-

def entrada_opcao():
    
    chave = 1   

    while chave == 1:
        opcao = input('Deseja calcular uma nova media? (1=SIM/0=NAO)')

        if opcao == 1 or opcao == 0:
            chave = 0
        else:
            chave = 1
            print 'Opcao invalida.'
    if opcao == 1:
        return True
    else:
        return False


if __name__ == '__main__':
    
    continua = entrada_opcao()
    print continua
