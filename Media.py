#!/usr/bin/python
# -*- coding: UTF-8 -*-

notas = []

for num in range(1,5):
    
    nota = float(input('Digite a nota ' + str(num) + ': '))
    
    while nota < 0 or nota > 10:
        nota = float(input('Nota inválida! Digite uma nota de 0 à 10: '))
        
    notas.append(nota)

media = sum(notas) / 4

print 'Sua média é: ' + str(media)