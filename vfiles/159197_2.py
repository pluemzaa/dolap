ic = float(input("Please enter your net income: "))

if  ic <= 150000:
      tax = 0
elif ic <= 300000:
      tax = (ic - 150000) * 0.05
elif  ic <= 500000:
      tax = ((ic - 300000) * 0.1) + 7500
elif  ic <= 750000:
      tax = ((ic - 500000) * 0.15) + 27500
elif  ic <= 1000000:
      tax = ((ic - 750000) * 0.2) + 65000
elif  ic <= 2000000:
      tax = ((ic - 1000000) * 0.25) + 115000
elif  ic <= 5000000:
      tax = ((ic - 2000000) * 0.3) + 365000
else:
      tax = ((ic - 5000000) * 0.35) + 1265000

print(f"The tax amount you have to pay this year : {tax:.2f}")