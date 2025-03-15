# 4. Inverter a Lista
# Escreva um programa que leia uma lista de palavras e exiba essa lista na ordem
# inversa.

list = []

n = int(input('How many words in the list:'))

for i in range(0,n):
    word = str(input(f'Word {i}:'))
    list.append(word)

list.reverse()
print(list)