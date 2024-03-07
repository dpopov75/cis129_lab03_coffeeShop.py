#Daniel Popov
#Coffee Shop Script
#Asks how many coffees and muffins the user would like to buy and calculates a total.
print('Coffee and Muffin Shop')
print('$5 per coffee and $4 per muffin')
Coffee = (input('''How many coffees would you like to buy?
'''))
Muffins = (input('''How many muffins would you like to buy?
'''))
NumCof = float(Coffee)
NumMuf = float(Muffins)
CofCost = (NumCof * 5)
MufCost = (NumMuf * 4)
TaxCost = (CofCost + MufCost)* 0.06
TaxFinal = round(TaxCost, 2)
TotalCost = CofCost + MufCost + TaxFinal
print('My Coffee and Muffin Shop Receipt')
print(Coffee,'Coffee at $5 each: $', CofCost)
print(Muffins, 'Muffins at $4 each: $', MufCost)
print('6% tax: $', TaxFinal)
print(' ----------')
print('Total: $' , TotalCost)


