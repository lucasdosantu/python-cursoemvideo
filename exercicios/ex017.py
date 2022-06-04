# Leia o comprimento do cateto oposto e adjacente de um triângulo e calcule a hipotenusa
from math import sqrt, hypot

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = sqrt(pow(co, 2) + pow(ca, 2))

print(f'A hipotenusa mede {hi:.2f}.\n')

hipo = hypot(co, ca)
print(f'math.hypot() == {hipo}')
