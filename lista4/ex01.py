# Lista de Exercícios - Trabalhando com Listas em Python
# 1. Soma dos Elementos de uma Lista
# Escreva um programa que solicite ao usuário uma lista de números inteiros e
# calcule a soma de todos os elementos da lista.

list = []
n = int(input('How many numbers in the list:'))

for i in range(0,n):
    number = int(input(f'Number {i}:'))
    list.append(number)

print(sum(list))