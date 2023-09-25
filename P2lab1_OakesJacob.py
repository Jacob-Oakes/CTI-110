#Jacob Oakes
#9/25/2023
#calclate cost of drving x amount of miles


mpg = float(input("Enter miles per gallon: "))
gas_price = float(input("Enter cost per gallon: "))

#calculate cost
twenty_miles = (20/mpg)*gas_price
seventyfive_miles = (75/mpg)*gas_price
fivehundred_miles = (500/mpg)*gas_price

#Displayed to user
print(f'The cost to drive 20 miles: {twenty_miles:.2f}')
print(f'The cost to drive 75 miles: {seventyfive_miles:.2f}')
print(f'The cost to drive 500 miles: {fivehundred_miles:.2f}')

