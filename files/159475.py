x = int(input("Please enter your net income:"))

if x >= 0 and x <= 150000 :
    tax = 0
elif x >= 150001 and x <= 300000 :
    tax = (x - 150000) * (5 / 100)
elif x >= 300001 and x <= 500000 :
    tax = (x - 300000) * (10 / 100) + 7500
elif x >= 500001 and x <= 750000 :
    tax = (x - 500000) * (15 / 100) + 27500
elif x >= 750001 and x <= 1000000 :
    tax = (x - 750000) * (20 / 100) + 65000
elif x >= 1000001 and x <= 2000000 :
    tax = (x - 1000000) * (25 / 100) + 115000
elif x >= 2000001 and x <= 5000000 :
    tax = (x - 2000000) * (30 / 100) + 365000
else :
    tax = (x - 5000000) * (35 / 100) + 1265000

print(f"The tax amount you have to pay this year : {tax:.2f}")