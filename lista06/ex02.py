# 2. Operações Matemáticas com Números em uma Tupla
# Solicite ao usuário quatro números inteiros e armazene-os em uma tupla. Em
# seguida, exiba:
# • Quantas vezes o número 9 apareceu na tupla.
# • Em que posição foi digitado o primeiro número 3 (caso exista).
# • Os números pares contidos na tupla.

numbers = tuple(int(input(f'Enter the {i+1}th number:')) for i in range(4))

print(f'The number 9 appeared {numbers.count(9)} times')

if 3 in numbers:
    print(f'The first number 3 appeared at position {numbers.index(3)}')
else:
    print('The number 3 was not entered')

count = 0
for number in numbers:
    if number % 2 == 0:
        count += 1

print(f'Even numbers: {count}')