# Lista de Exercícios - Trabalhando com Dicionários em Python
# 1. Cadastro de Alunos
# Crie um programa que permita cadastrar alunos em um dicionário. O programa
# deve solicitar o nome e a nota do aluno e armazená-los como chave e valor no
# dicionário. Após a inserção de pelo menos 3 alunos, exiba a lista de alunos e suas
# respectivas notas.

def register_students():
    students = {}

    while input('Would you like to add a student? (y/n):').lower() == 'y':
        name = input('Enter student name:')
        grade = float(input('Enter student grade:'))
        students[name] = grade

    print('Students and Grades:')
    for name, grade in students.items():
        print(f'{name}: {grade}')


register_students()