# 2. Verificação de Número Primo
# Crie uma função que receba um número inteiro e retorne True se for primo e False
# caso contrário. No programa principal, solicite um número ao usuário e utilize a
# função para verificar se ele é primo.

def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input('Digite um número:'))

if primo(num):
    print(f'{num} é primo')
else:
    print(f'{num} não é primo')