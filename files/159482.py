num = int(input("Please enter your net income: "))
if num <= 150000:
    tax = 0
elif num >= 150001 and num <= 300000:
    tax = (num - 150000) * 0.05
elif num >= 300001 and num <= 500000:
    tax = (num - 300000) * 0.1 + 7500
elif num >= 500001 and num <= 750000:
    tax = (num - 500000) * 0.15 + 27500
elif num >= 750001 and num <= 1000000:
    tax = (num - 750000) * 0.2 + 65000
elif num >= 1000001 and num <= 2000000:
    tax = (num - 1000000) * 0.25 + 115000
elif num >= 2000001 and num <= 5000000:
    tax = (num - 2000000) * 0.30 + 365000
elif num > 5000000:
    tax = (num - 5000000) * 0.35 + 1265000
else:
    tax = (num - 2000000) * 0.3 + 240000
print(f"The tax amount you have to pay this year : {tax:.2f} ")