# 5. Contar Ocorrências de um Elemento
# Escreva um programa que peça ao usuário para inserir uma lista de números e um
# número específico. O programa deve contar quantas vezes esse número aparece
# na lista.

list = []

esp_n = int(input('Type a especific number:'))
n = int(input('How many number in the list:'))

count = 0
for i in range(0,n):
    number = int(input(f'Number {i}:'))
    list.append(number)
    if number == esp_n:
        count += 1

print(f'Your especific number appers: {count} times in the list')
