# 4. Números Ímpares em um Intervalo
# Peça ao usuário dois números inteiros, representando um intervalo A,B. O programa deve
# exibir todos os números ímpares dentro desse intervalo (inclusive os limites, se forem
# ímpares).

num1 = int(input('Digite o primeiro número inteiro:'))

num2 = int(input('Digite o segundo número inteiro:'))

for num in range(num1, num2 + 1):
    if(num % 2 != 0):
        print(num)