# 4. Nomes de Alunos e Notas
# Crie uma tupla que armazene o nome de cinco alunos e suas respectivas notas
# (ex: ('Ana', 8.5, 'Carlos', 7.0, 'Beatriz', 9.2, 'Daniel', 6.8, 'Eduarda', 8.0)). Depois, exiba
# apenas os nomes dos alunos e, em seguida, apenas as notas.

students_grades = ('Ana', 8.5, 'Carlos', 7.0, 'Beatriz', 9.2, 'Daniel', 6.8, 'Eduarda', 8.0)

names = students_grades[::2]
print(names)

grades = students_grades[1::2]
print(grades)