# Lista de Exercícios - Tratamento de Exceções em Python
# 1. Divisão Segura
# Crie um programa que solicite ao usuário dois números e realize a divisão do
# primeiro pelo segundo. Utilize tratamento de exceções para evitar erros de
# divisão por zero e erros de entrada inválida (como caracteres não numéricos).

def divisao_segura():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 / num2
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero!")
    except ValueError:
        print("Erro: Entrada inválida! Por favor, digite apenas números.")
    else:
        print(f"O resultado da divisão é: {resultado}")

divisao_segura()