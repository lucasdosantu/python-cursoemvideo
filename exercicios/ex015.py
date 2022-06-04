# Car rent
# Distance traveled and days rented.
# $60 per day and $0,15 per distance traveled

days = int(input('How many days rented? '))
distance = float(input('Distance traveled? '))

rentPrice = (days * 60) + (distance * .15)

print(f'Car was rented for {days} days and traveled {distance:.2f} distance.\n'
      f'Total to pay is ${rentPrice:.2f}.')
