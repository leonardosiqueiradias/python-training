# 4. Cálculo de Média e Aprovação
# Elabore um programa que solicite duas notas ao usuário e calcule a média. Em seguida,
# informe se o aluno foi:
# • Aprovado (média maior ou igual a 7)
# • Recuperação (média entre 5 e 6.9)
# • Reprovado (média abaixo de 5)

nota1 = float(input('Digite a primeiro nota do usuário:'))
nota2 = float(input('Digite a segunda nota do usuário:'))

media = (nota1 + nota2)/2

if(media >= 7):
    print('Aprovado')
elif(media >= 5 and media <= 6.9):
    print('Recuperação')
else:
    print('Reprovado')