# 5. Operações Bancárias com Tratamento de Erros
# Crie um programa que simule um sistema bancário simples. O saldo inicial do
# usuário é de R$ 1000,00. O programa deve permitir que o usuário insira um valor
# para saque e, caso o valor solicitado seja maior que o saldo disponível, uma
# exceção personalizada deve ser lançada informando que o saldo é insuficiente.

class SaldoInsuficiente(Exception):
    pass

def operacoes_bancarias():
    saldo = 1000.00
    try:
        saque = float(input(f"Seu saldo é R$ {saldo}. Qual valor deseja sacar? "))
        if saque > saldo:
            raise SaldoInsuficiente("Erro: Saldo insuficiente para realizar o saque.")
        saldo -= saque
        print(f"Operação realizada com sucesso! Novo saldo: R$ {saldo}.")
    except SaldoInsuficiente as e:
        print(e)
    except ValueError:
        print("Erro: Valor inválido! Por favor, digite um número válido para o saque.")

operacoes_bancarias()