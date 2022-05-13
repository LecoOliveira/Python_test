''' Exercício consiste em achar o primeiro número repetido em uma lista,
caso a lista não contenha, retornar -1.'''

liste_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 8, 7, 5, 9, 1, 4, 2, 1, 5],
    [1, 2, 5, 2, 3, 5, 4, 7, 4, 10],
    [10, 9, 8, 7, 6, 6, 5, 4, 3, 2],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    [10, 9, 5, 7, 6, 5, 4, 3, 2, 1]
]

def primeiro_duplicado(lista_referencia):
    resultado = {}
    for marcador, lista in enumerate(lista_referencia):
        lista_nova = []
        for numero in lista:
            if numero not in lista_nova:
                lista_nova.append(numero)
                if len(lista_nova) == 9:
                    resultado[marcador + 1] = -1
            else:
                resultado[marcador + 1] = numero
                break
        if resultado[marcador + 1] != -1:
            print(f'O primeiro número a se repetir na lista {marcador + 1} é o {resultado[marcador + 1]}.')
        else:
            print(f'A lista {marcador + 1} não contém números repetidos, logo {resultado[marcador + 1]}.')
            



primeiro_duplicado(liste_de_listas_de_inteiros)