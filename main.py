"""
This program calculates prices for custom house signs.
"""
charge = 0.00
minCharge = 35.00
numChars = 18
color = 'black'
woodType = 'oak'

if numChars > 5:
  charge = minCharge + ((numChars - 5.00) * 4.00) 
else:
  charge = minCharge
if color == 'gold':
  charge = charge + 15.00
if woodType == 'oak':
  charge = charge + 20.00
if charge < 35.00:
  charge = 35.00
  
print("The charge for this sign is $" + str(charge))
