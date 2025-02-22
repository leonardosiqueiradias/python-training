# Lista de Exercícios – Estrutura Sequencial em Python
# 1. Cálculo da Área do Círculo
# Escreva um programa que peça ao usuário o valor do raio de um círculo e calcule sua área.
# Use a fórmula:

# Dica: Use math.pi para obter o valor de π.

import math

raio = int(input('Qual o raio do círculo?'))


area = math.pi*(raio*raio)

print(f'A área do círculo: {area}')