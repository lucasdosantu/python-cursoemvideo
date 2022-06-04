# Leia um ângulo qualquer e mostre o valor do seno, cos e tan
from math import sin, cos, tan, radians
ang = float(input('Escreva um ângulo: '))
rad = radians(ang)
sen = sin(rad)
cos = cos(rad)
tan = tan(rad)

print(f'O SENO de {ang}º é {sen:.2}.')
print(f'O COSSENO de {ang}º é {cos:.2}.')
print(f'A TANGENTE de {ang}º é {tan:.2}.')
