# 4. Contador de Vogais em uma Palavra
# Crie uma função que receba uma palavra como parâmetro e retorne a quantidade
# de vogais presentes nela. No programa principal, solicite uma palavra ao usuário e
# utilize a função para exibir o número de vogais.

def contar_vogais(palavra):
    vogais = "aeiouAEIOU"  # Lista de vogais maiúsculas e minúsculas
    contador = sum(1 for letra in palavra if letra in vogais)  # Conta quantas vogais há na palavra
    return contador

palavra = input("Digite uma palavra: ")
print(f"A palavra '{palavra}' contém {contar_vogais(palavra)} vogais.")