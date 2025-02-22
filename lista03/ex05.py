# 5. Sequência de Fibonacci
# Escreva um programa que peça ao usuário um número N e exiba os N primeiros termos da
# Sequência de Fibonacci.
# Obs: A sequência de Fibonacci começa com 0 e 1, e cada termo seguinte é a soma dos dois
# anteriores:

num = int(input('Digite um número:'))

# Inicializa os dois primeiros termos da sequência de Fibonacci
a, b = 0, 1

# Exibe os N primeiros termos
for i in range(num):
    print(a, end=" ")
    a, b = b, a + b  # Atualiza os termos da sequência