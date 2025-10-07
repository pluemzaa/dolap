a = float(input("Please enter your net income: "))

if a <= 150000:
    b = 0
elif a <= 300000:
    b = (a - 150000) * 0.05
elif a <= 500000:
    b = ((a - 300000) * 0.1) + 7500
elif a <= 750000:
    b = ((a - 500000) * 0.15) + 27500
elif a <= 1000000:
    b = ((a - 750000) * 0.2) + 65000
elif a <= 2000000:
    b = ((a - 1000000) * 0.25) + 115000
elif a <= 5000000:
    b = ((a - 2000000) * 0.3) + 365000
else:
    b = ((a - 5000000) * 0.35) + 1265000
print(f"The tax amount you have to pay this year : {b:.2f}")