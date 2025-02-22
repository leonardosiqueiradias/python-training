# 2. Maior Número
# Faça um programa que peça dois números ao usuário e exiba o maior deles. Caso os números
# sejam iguais, exiba uma mensagem informando essa condição.

num01 = float(input('Digite o primeiro número:'))
num02 = float(input('Digite o segundo número:'))

if(num01 > num02):
    print(f'O maior número é o primeiro: {num01}')
elif(num02 > num01):
    print(f'O maior número é o segundo: {num02}')
elif(num01 == num02):
    print(f'Os dois números são iguais')