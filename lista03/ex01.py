# Lista de Exercícios – Estrutura de Repetição em Python
# 1. Contagem Progressiva
# Escreva um programa que peça um número inteiro positivo ao usuário e exiba todos os
# números de 1 até esse número, um por linha.

numero = int(input('Digite um número inteiro positivo:'))

for x in range(numero):
    print(x+1)