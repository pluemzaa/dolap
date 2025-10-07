income = float(input('Please enter your net income: '))

if income <= 150000:
    vat = 0
elif income <= 300000:
    vat = (income - 150000) * 0.05
elif income <= 500000:
    vat = (income - 300000) * 0.10 + 7500
elif income <= 750000:
    vat = (income - 500000) * 0.15 + 27500
elif income <= 1000000:
    vat = (income - 750000) * 0.20 + 65000
elif income <= 2000000:
    vat = (income - 1000000) * 0.25 + 115000
elif income <= 5000000:
    vat = (income - 2000000) * 0.30 + 365000
else:
    vat = (income - 5000000) * 0.35 + 1265000

print(f'The tax amount you have to pay this year : {vat:.2f}')