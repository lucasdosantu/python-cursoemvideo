import math
# Operadores aritméticos

#   +     adição
#   -     subtração
#   *     multriplicação
#   /     divisão
#   **    potência
#   //    divisão inteira
#   %     resto da divisão

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
a = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
re = n1 % n2
p = n1 ** n2

print(f'Você digitou {n1} e {n2}.\n'
      f'A soma é {a}.\n'
      f'A subtração é {s}.\n'
      f'O produto é {m}.\n'
      f'A divisão é {d:.2f}.\n'
      f'A divisão inteira é {di} e o resto é {re}.\n'
      f'A potência de {n1}^{n2} é {p}.')
