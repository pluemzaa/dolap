Net_income = int(input("Please enter your net income: "))
Tax_amount = 0.0

if Net_income <= 150000:
    Tax_amount = 0.0
elif Net_income <= 300000:
    Tax_amount = (Net_income - 150000) * 0.05
elif Net_income <= 500000:
    Tax_amount = (Net_income - 300000) * 0.10 + 7500
elif Net_income <= 750000:
    Tax_amount = (Net_income - 500000) * 0.15 + 27500
elif Net_income <= 1000000:
    Tax_amount = (Net_income - 750000) * 0.20 + 65000
elif Net_income <= 2000000:
    Tax_amount = (Net_income - 1000000) * 0.25 + 115000
elif Net_income <= 5000000:
    Tax_amount = (Net_income - 2000000) * 0.30 + 365000
else:
    Tax_amount = (Net_income - 5000000) * 0.35 + 1265000

print("The tax amount you have to pay this year : %.2f" % Tax_amount)