try:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    resultado = a / b
except ZeroDivisionError:
    print("Erro: Divisão por zero!")
except ValueError:
    print("Erro: Entrada inválida!")
else:
    print("Resultado:", resultado)