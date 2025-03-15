# Lista de Exercícios - Trabalhando com Funções em Python
# 1. Cálculo do Fatorial
# Crie uma função que receba um número inteiro como parâmetro e retorne o seu
# fatorial. Em seguida, utilize essa função em um programa principal para calcular o
# fatorial de um número informado pelo usuário.

def fat(n):
    result = 1
    cont = 1

    while cont <= n:
        result *= cont
        cont += 1
    return result

n = int(input('Fatorial de:'))
print(fat(n))
