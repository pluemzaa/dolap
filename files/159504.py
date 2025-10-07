m = float(input("Please enter your net income:"))
tax = 0
if m <= 150000:
    tax = 0
elif m <= 300000:
    tax = (m - 150000) * 0.05
elif m <= 500000:
    tax = ((m - 300000) * 0.10) + 7500
elif m <= 750000:
    tax = ((m - 500000) * 0.15) + 27500
elif m <= 1000000:
    tax = ((m - 750000) * 0.20) + 65000
elif m <= 2000000:
    tax = ((m - 1000000) * 0.25) + 115000
elif m <= 5000000:
    tax = ((m - 2000000) * 0.30) + 365000
else:
    tax = ((m - 5000000) * 0.35) + 1265000
print(f"The tax amount you have to pay this year :{tax:.2f}")