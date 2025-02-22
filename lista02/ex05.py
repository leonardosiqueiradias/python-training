# 5. Verificação de Triângulo
# Peça ao usuário três números representando os lados de um triângulo. O programa deve
# verificar e informar se os valores formam um triângulo válido (a soma de dois lados deve ser
# sempre maior que o terceiro).

lado1 = float(input('Digite o lado 1 do triângulo:'))

lado2 = float(input('Digite o lado 2 do triângulo:'))

lado3 = float(input('Digite o lado 3 do triângulo:'))

if(lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1):
    print('É um triângulo')
else:
    print('Não é um triângulo!')