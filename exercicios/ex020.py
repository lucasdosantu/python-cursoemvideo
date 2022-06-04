# Read for names, choose a order and show it order

from random import sample

a = str(input('Name 1: '))
b = str(input('Name 2: '))
c = str(input('Name 3: '))
d = str(input('Name 4: '))
names = [a, b, c, d]
order = sample(names, len(names))

print(f'The chosed order was: {order}.')
