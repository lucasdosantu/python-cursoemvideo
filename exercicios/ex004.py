n = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(n)}.\n'
      f'Só tem espaços? {n.isspace()}\n'
      f'É um número? {n.isnumeric()}\n'
      f'É alfanumérico? {n.isalnum()}\n'
      f'É alfabético? {n.isalpha()}\n'
      f'Está em maiúsculas? {n.isupper()}\n'
      f'Está em minúsculas? {n.islower()}\n'
      f'Está capitalizado? {n.istitle()}')
