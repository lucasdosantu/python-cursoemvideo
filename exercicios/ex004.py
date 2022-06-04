n = input('Type anything: ')
print(f'You typped a {type(n)}.\n'
      f'Only spaces? {n.isspace()}\n'
      f'Is it a number? {n.isnumeric()}\n'
      f'Is it alphanumeric? {n.isalnum()}\n'
      f'Is it alphabetic? {n.isalpha()}\n'
      f'Is it uppercase? {n.isupper()}\n'
      f'Is it lowercase? {n.islower()}\n'
      f'Is it captalized? {n.istitle()}')
