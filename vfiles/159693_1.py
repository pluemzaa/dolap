x = int(input("Please enter your net income: "))


tax = 0.0
if x <= 150000:
    tax = 0.0
elif x <= 300000:
    tax = (x - 150000) * 0.05
elif x <= 500000:
    tax = ((x - 300000) * 0.10) + 7500
elif x <= 750000:
    tax = ((x - 500000) * 0.15) + 27500    
elif x <= 1000000:
    tax = ((x - 750000) * 0.20) + 65000
elif x <= 2000000:
    tax = ((x - 1000000) * 0.25) + 115000
elif x <= 5000000:
    tax = ((x - 2000000) * 0.30) + 365000
else:
    tax = ((x - 5000000) * 0.35) + 1265000
print(f"The tax amount you have to pay this year : {tax:.2f}")