# Read height and width, calc the area and calc how many liters of ink is necessary to paint the whole area
# (consider 1L paint 2m²)

h = float(input('Height? '))
l = float(input('Width? '))

a = h * l
t = a / 2.

print(f'The wall have {h}x{l}m and it area is {a:.2f}m²\n'
      f'It will be necessary {t:.2f}L of ink to paint the whole area.')

