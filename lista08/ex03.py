# 3. Conversão de Entrada com Exceções
# Crie um programa que peça ao usuário para digitar um número inteiro. O programa
# deve tentar converter a entrada e exibir o dobro desse número. Caso o usuário
# digite um valor inválido, o programa deve exibir uma mensagem de erro e solicitar
# a entrada novamente até que um número válido seja fornecido.

def conversao_entrada():
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            print(f"O dobro do número é: {numero * 2}")
            break
        except ValueError:
            print("Erro: Entrada inválida! Por favor, digite um número inteiro válido.")

conversao_entrada()