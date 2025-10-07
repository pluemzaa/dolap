i = int(input("Please enter your net income: "))

tax = 0

if i > 5000000:
    tax = ((i - 5000000) * 0.35) + 1265000
elif i > 2000000:
    tax = ((i - 2000000) * 0.3) + 365000
elif i > 1000000:
    tax = ((i - 1000000) * 0.25) + 115000
elif i > 750000:
    tax = ((i - 750000) * 0.2) + 65000
elif i > 500000:
    tax = ((i - 500000) * 0.15) + 27500
elif i > 300000:
    tax = ((i - 300000) * 0.1) + 7500
elif i > 150000:
    tax = ((i - 150000) * 0.05)

print("The tax amount you have to pay this year : %.2f" %tax)