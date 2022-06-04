# Calc hypotenuse with oposite and adjacent side.

from math import sqrt

co = float(input('Oposite side: '))
ca = float(input('Adjacent side: '))
hi = sqrt(pow(co, 2) + pow(ca, 2))

print(f'Hypotenuse is {hi:.2f}.\n')
