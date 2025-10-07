a = float(input("Please enter your net income: "))
tax = 1
if a >= 0 and a <= 150000:
    print("The tax amount you have to pay this year : 0.00")
elif a >= 150001 and a <= 300000:
    tax = (a -150000) * 0.05
    print(f"The tax amount you have to pay this year : {tax:.2f}")
elif a >= 300001 and a <= 500000:
    tax = (a - 300000) * 10 + 7500
    print(f"The tax amount you have to pay this year : {tax:.2f}")
elif a >= 500001 and a <= 750000:
    tax = (a - 500000) * 0.15 + 27500
    print(f"The tax amount you have to pay this year : {tax:.2f}")
elif a >= 750001 and a <= 1000000:
    tax = (a -750000) * 0.2 + 65000
    print(f"The tax amount you have to pay this year : {tax:.2f}")
elif a >= 1000001 and a <= 2000000:
    tax (a - 1000000) * 0.25 + 115000
    print(f"The tax amount you have to pay this year : {tax:.2f}")
elif a >= 2000001 and a <= 5000000:
    tax = (a - 2000000) * 0.3 + 365000
    print(f"The tax amount you have to pay this year : {tax:.2f}")
else:
    a > 5000000
    tax = (a - 5000000) * 0.35 + 1265000
    print(f"The tax amount you have to pay this year : {tax:.2f}")