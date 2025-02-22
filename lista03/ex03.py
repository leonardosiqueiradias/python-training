# 3. Tabuada de um Número
# Peça um número inteiro ao usuário e exiba a tabuada desse número de 1 a 10.

num = int(input('Digite um número:'))

for x in range(1,11):
    print(f'Tabuada de {x}: {num*x}')