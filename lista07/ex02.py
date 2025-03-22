# 2. Contagem de Caracteres em uma Palavra
# Escreva um programa que solicite ao usuário uma palavra e utilize um dicionário
# para armazenar a contagem de cada caractere presente na palavra. Exiba o
# dicionário ao final.

count_character = {}

word = input('Enter a word:')

count = len(word)

count_character[word] = count

for word, count in count_character.items():
    print(f'{word}: {count}')