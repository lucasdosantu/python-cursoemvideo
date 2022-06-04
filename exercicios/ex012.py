# Read the price of a product and show it price with 5% discount

price = float(input('What is your product price?\nUS$ '))
discount = price - (price * .05)

print(f'From US$ {price:.2f} for US$ {discount:.2f} with 5% discount.')
