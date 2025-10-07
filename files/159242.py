i = float(input("Please enter your net income: "))

if i <= 150000:
  vat = 0
elif i <= 300000:
  vat = (i - 150000) * 0.05
elif i <= 500000:
  vat = (i - 300000) * 0.10 + 7500
elif i <= 750000:
  vat = (i - 500000) * 0.15 + 27500
elif i <= 1000000:
  vat = (i - 750000) * 0.20 + 65000 
elif i <= 2000000:
  vat = (i - 1000000) * 0.25 + 115000
elif i <= 5000000:
  vat = (i - 2000000) * 0.30 + 365000
else:
  vat = (i - 5000000) * 0.35 + 1265000

print(f"The tax amount you have to pay this year : {vat:.2f}")