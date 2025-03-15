# 3. Cálculo da Média de uma Lista
# Crie uma função que receba uma lista de números e retorne a média dos valores.
# No programa principal, peça ao usuário para inserir os números e exiba a média
# utilizando a função criada.

def media(list):
    soma = sum(list)
    return soma / len(list) if len(list) > 0 else 0

list = []
n = int(input('How many numbers in list:'))

for i in range(n):
    number = float(input(f'Number {i}:'))
    list.append(number)

print(f'Média da lista:{media(list)}')