# Read four names and choose one of them

from random import choice

a = str(input('Name 1: '))
b = str(input('Name 2: '))
c = str(input('Name 3: '))
d = str(input('Name 4: '))

names = [a, b, c, d]

chosen = choice(names)

print(f'Chosen was {chosen}.')
