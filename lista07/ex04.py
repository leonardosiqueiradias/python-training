# 4. Estatísticas de um Texto
# Peça ao usuário para inserir uma frase. Utilize um dicionário para armazenar a
# contagem de palavras, ou seja, a chave será a palavra e o valor será o número de
# vezes que ela aparece na frase. Exiba o dicionário ao final.

phrase = input('Enter a phrase:')

words = phrase.split()
count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

print('Contagem de palavras:')
print(count)