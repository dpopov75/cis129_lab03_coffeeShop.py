#Daniel Popov
#Coffee Shop Script
#Asks how many coffees, muffins, brownies, and burritos the user would like to buy and calculates a total based on pre-set prices
print("Daniels Cafe")
print('$5 per coffee, $4 per muffin, $6 per brownie, $2.50 per burrito')
Coffee = input('''How many coffees would you like to buy?
''')
Muffin = input('''How many muffins would you like to buy?
''')
Brownie = input('''How many brownies would you like to buy?
''')
Burrito = input('''How many burritos would you like to buy?
''')
NumCof = float(Coffee)
NumMuf = float(Muffin)
NumBro = float(Brownie)
NumBur = float(Burrito)
CofCost = (NumCof * 5)
MufCost = (NumMuf * 4)
BroCost = (NumBro * 6)
BurCost = (NumBur * 2.5)
TaxCost = (CofCost + MufCost + BroCost + BurCost)* 0.06
TaxFinal = round(TaxCost, 2)
TotalCost = CofCost + MufCost + BroCost + BurCost + TaxFinal
print('My Cafe Receipt')
print(Coffee,'Coffee at $5 each: $', CofCost)
print(Muffin, 'Muffins at $4 each: $', MufCost)
print(Brownie, 'Brownies at $6 each: $', BroCost)
print(Burrito, 'Burritos at $2.50 each: $', BurCost)
print('6% tax: $', TaxFinal)
print(' ----------')
print('Total: $' , TotalCost)
print("Thank you for shopping")


