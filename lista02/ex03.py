# 3. Classificação de Idade
# Crie um programa que peça a idade de uma pessoa e informe sua classificação:
# • Menor de idade (menos de 18 anos)
# • Adulto (entre 18 e 59 anos)
# • Idoso (60 anos ou mais)

idade = int(input('Digite a sua idade:'))

if(idade < 18):
    print('Você é menor de idade')
elif(idade >= 18 and idade < 59):
    print('Você é Adulto')
elif(idade >= 60):
    print('Você é um Idoso')