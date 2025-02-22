# 2. Conversão de Temperatura
# Faça um programa que leia uma temperatura em graus Celsius e a converta para Fahrenheit.
# A fórmula de conversão é:

# O programa deve exibir o valor convertido.

graus_celsius = float(input('Digite uma temperatura em graus celsius:'))

fahrenheit = (graus_celsius * 9.5) + 32

print(f'Esta temperatura em fahrenheit é:{fahrenheit}')