# 2. Encontrar o Maior e o Menor Número
# Escreva um programa que leia uma lista de números digitados pelo usuário e
# determine o maior e o menor número presentes na lista.

list = []

n = int(input('How many numbers in the list:'))

for i in range(0,n):
    number = int(input(f'Number {i}:'))
    list.append(number)

print(f'min number:{min(list)}')
print(f'max number:{max(list)}')