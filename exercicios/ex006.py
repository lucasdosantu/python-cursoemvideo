# Algoritmo que leia um número e mostre o seu dobro, seu triplo e raiz quadrada

n = int(input('Digite um valor: '))
d = n * 2
t = n * 3
r = n ** (1/2)

print(f'O dobro de {n} é {d}.\n'
      f'O triplo de {n} é {t}.\n'
      f'A raiz quadrada de {n} é {r:.2f}.')
