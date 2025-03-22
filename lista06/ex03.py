# 3. Listagem de Cores do Arco-Íris
# Crie uma tupla contendo as cores do arco-íris em ordem. Depois, permita que o
# usuário informe um número de 1 a 7 e exiba a cor correspondente.


tuple = ('Red','Orange','Yellow','Green','Blue','Indigo','Violet')

n = int(input('Enter a number to know the corresponding color:'))

if 1 <= n <= 7:
    print(f'The corresponding color is: {tuple[n-1]}')
else:
    print('Invalid number!')