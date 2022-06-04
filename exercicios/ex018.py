# Calc sin, cos and tan of an angle

from math import sin, cos, tan, radians
ang = float(input('Type an angle: '))
rad = radians(ang)
sen = sin(rad)
cos = cos(rad)
tan = tan(rad)

print(f'SIN of {ang}º is {sen:.2}.')
print(f'COS of {ang}º is {cos:.2}.')
print(f'TAN of {ang}º is {tan:.2}.')
