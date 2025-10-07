print("Please enter your net income:")
net_income_input = input()
net_income = float(net_income_input)
tax_amount = 0.0

if net_income >= 0 and net_income <= 150000:
    tax_amount = 0.0
elif net_income > 150000 and net_income <= 300000:
    tax_amount = (net_income - 150000) * 0.05
elif net_income > 300000 and net_income <= 500000:
    tax_amount = ((net_income - 300000) * 0.10) + 7500.0
elif net_income > 500000 and net_income <= 750000:
    tax_amount = ((net_income - 500000) * 0.15) + 27500.0
elif net_income > 750000 and net_income <= 1000000:
    tax_amount = ((net_income - 750000) * 0.20) + 65000.0
elif net_income > 1000000 and net_income <= 2000000:
    tax_amount = ((net_income - 1000000) * 0.25) + 115000.0
elif net_income > 2000000 and net_income <= 5000000:
    tax_amount = ((net_income - 2000000) * 0.30) + 365000.0
elif net_income > 5000000:
    tax_amount = ((net_income - 5000000) * 0.35) + 1265000.0
else:
    print("Error: Net income cannot be negative.")
    tax_amount = 0.0 

print("The tax amount you have to pay this year: %.2f" % tax_amount)