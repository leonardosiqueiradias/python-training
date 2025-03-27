# 4. Acesso a Elementos de uma Lista
# Crie uma lista com cinco números e permita que o usuário informe um índice para
# acessar um valor da lista. Utilize tratamento de exceções para evitar erros caso o
# usuário digite um índice inválido.

def acesso_lista():
    lista = [10, 20, 30, 40, 50]
    try:
        indice = int(input("Digite o índice para acessar um valor da lista (0 a 4): "))
        print(f"O valor no índice {indice} é: {lista[indice]}")
    except IndexError:
        print("Erro: Índice inválido! O índice deve estar entre 0 e 4.")
    except ValueError:
        print("Erro: Por favor, digite um número válido para o índice.")

acesso_lista()