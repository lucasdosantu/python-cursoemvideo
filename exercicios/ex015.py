# Aluguel de carro
# KM percorrido e a quantidade de dias alugados.
# sabe-se que R$ 60 por dia  R$ 0,15 por KM rodado

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))

aluguel = (dias * 60) + (km * .15)

print(f'O carro foi alugado por {dias} dias e rodou {km:.2f}KM.\n'
      f'O total a ser pago pelo aluguel é R$ {aluguel:.2f}.')
