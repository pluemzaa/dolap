net_money = float(input("Please enter your net income: "))

if net_money <= 150000:
    tax = 0
elif net_money <= 300000:
    tax = (net_money - 150000) * 0.05
elif net_money <= 500000:
    tax = (net_money - 300000) * 0.10 + 7500
elif net_money <= 750000:
    tax = (net_money - 500000) * 0.15 + 27500
elif net_money <= 1000000:
    tax = (net_money - 750000) * 0.20 + 65000
elif net_money <= 2000000:
    tax = (net_money - 1000000) * 0.25 + 115000
elif net_money <= 5000000:
    tax = (net_money - 2000000) * 0.30 + 365000
else:
    tax = (net_money - 5000000) * 0.35 + 1265000
print(f"The tax amount you have to pay this year : {tax:.2f}")