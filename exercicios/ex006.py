# Algorithm that read a number and show it double, triple and square root.

n = int(input('Type a number: '))
d = n * 2
t = n * 3
r = n ** (1/2)

print(f'Double of {n} is {d}.\n'
      f'Triple of {n} is {t}.\n'
      f'Square root of {n} is {r:.2f}.')
