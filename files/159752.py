n = float(input("Please enter your net income: "))
if n <= 150000:
    tax = 0
elif n <= 300000:
    tax = (n - 150000) * 0.05
elif n <= 500000:
    tax = (n - 300000) * 0.10 + 7500
elif n <= 750000:
    tax = (n - 500000) * 0.15 + 27500
elif n <= 1000000:
    tax = (n - 750000) * 0.20 + 65000
elif n <= 2000000:
    tax = (n - 1000000) * 0.25 + 115000
elif n <= 5000000:
    tax = (n - 2000000) * 0.30 + 365000
else:
    tax = (n - 5000000) * 0.35 + 1265000
print(f"The tax amount you have to pay this year : {tax:.2f}")