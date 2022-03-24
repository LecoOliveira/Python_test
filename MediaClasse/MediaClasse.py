# -*- coding: utf-8 -*-

import entrada

media, media_turma, qtd_alunos, acumula_media = 0, 0, 0, 0
continua = True

def soma(n):
    soma_nota = 0
    for nota in notas:
        soma_nota += nota
    return soma_nota

while continua:
    notas = []
    
    entrada.entrada_nota(notas)
    
    media = float(soma(notas) / 4)
    acumula_media += media
    qtd_alunos += 1

    if media >= 7:
        print '\nAluno aprovado com media ' + str(round(media, 1)) + '!'
    else:
        print '\nAluno reprovado com media ' + str(round(media, 1)) + '!'    
    
    continua = entrada.entrada_opcao()

media_turma = acumula_media / qtd_alunos

print '\nA media da turma foi: ' + str(float(round(media_turma, 1))) + '!'
    