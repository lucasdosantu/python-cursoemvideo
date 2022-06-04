# Leia quatro nomes, sorteie e mostre e a ordem de apresentação
from random import sample

a = str(input('Aluno 1: '))
b = str(input('Aluno 2: '))
c = str(input('Aluno 3: '))
d = str(input('Aluno 4: '))
alunos = [a, b, c, d]
ordem = sample(alunos, len(alunos))

print(f'A ordem escolhida foi: {ordem}.')