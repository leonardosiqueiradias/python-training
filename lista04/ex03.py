# 3. Remover Duplicatas
# Escreva um programa que leia uma lista de números e remova os valores
# duplicados, mantendo a ordem original.

list = []

n = int(input('How many numbers in the list:'))

for i in range(0,n):
    number = int(input(f'Number {i}:'))
    list.append(number)

print(set(list))