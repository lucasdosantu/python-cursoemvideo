# Leia altura e largura de uma parede e calcule a área da parede e a quantidade de tinta necessária para pintar (considerando que 1L de tinta pinta 2m²)

h = float(input('Qual a altura da parede? '))
l = float(input('Qual a largura da parede? '))

a = h * l
t = a / 2.

print(f'Sua parede possui tem dimensão de {h}x{l} e sua área é de {a:.2f}m²\n'
      f'Serão necessários {t:.2f}L de tinta.')

