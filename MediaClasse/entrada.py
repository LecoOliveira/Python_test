
# -*- coding: utf-8 -*-

def entrada_nota(notas):
    controle = 1
    while controle < 5:
       notas.append(input("Informe a " + str(controle) + "° nota: "))
       controle += 1
    
        
if __name__ == '__main__':
    notas = []
    entrada_nota()
    print notas
