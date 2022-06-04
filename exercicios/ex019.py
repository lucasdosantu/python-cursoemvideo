# Leia quatro nomes e sorteie um deles
from random import choice

a = str(input('Aluno 1: '))
b = str(input('Aluno 2: '))
c = str(input('Aluno 3: '))
d = str(input('Aluno 4: '))

alunos = [a, b, c, d]

escolhido = choice(alunos)

print(f'O escolhido foi {escolhido}.')
