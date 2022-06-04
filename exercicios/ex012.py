# Leia o preço de um produto e mostre o preço com 5% de desconto.

preco = float(input('Qual o valor do produto?\nR$ '))
desconto = preco - (preco * .05)

print(f'De R$ {preco:.2f} por R$ {desconto:.2f} com 5% de desconto.')
