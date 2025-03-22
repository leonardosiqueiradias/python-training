# 3. Dicionário de Tradução
# Crie um dicionário que contenha algumas palavras em português como chave e
# suas respectivas traduções para inglês como valor. Permita que o usuário digite
# uma palavra em português e retorne sua tradução. Caso a palavra não esteja no
# dicionário, exiba uma mensagem informando que a tradução não foi encontrada.

translation = {
    'gato': 'cat',
    'cachorro': 'dog',
    "casa": "house",
    "carro": "car",
    "livro": "book"
}

word = input('Enter a portuguese word:').strip().lower()

if word in translation:
    print(f"The translation of {word} is '{translation[word]}'.")
else:
    print('The word was not found.')