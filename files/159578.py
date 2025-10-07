x = int(input("Please enter your net income: "))

if x <= 150000:
    z = 0
elif x<= 300000:
    z = (x - 150000) * 0.05
elif x <= 500000:
    z = ((x - 300000) * 0.1) + 7500
elif x <= 750000:
    z = ((x - 500000) * 0.15) + 27500
elif x <= 1000000:
    z = ((x - 750000) * 0.2) + 65000
elif x <= 2000000:
    z = ((x - 1000000) * 0.25) + 115000
elif x <=  5000000:
    z = ((x - 2000000) * 0.3) + 365000
elif x > 5000000:
    z = ((x - 5000000) * 0.35) + 1265000

print(f"The tax amount you have to pay this year : {z:.2f}")