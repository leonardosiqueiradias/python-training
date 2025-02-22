# 4. Cálculo do Salário Mensal
# Faça um programa que pergunte o número de horas trabalhadas no mês e o valor recebido
# por hora. O programa deve calcular e exibir o salário total do mês.

horas_trabalhadas = float(input('Digite o número de horas trabalhadas no mês:'))

recebido_por_hora = float(input('Valor recebido por hora:'))

salario = horas_trabalhadas*recebido_por_hora

print(f'Seu salário:{salario} reais')

