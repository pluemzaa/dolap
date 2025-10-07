income = int(input("Please enter your net income:"))

if income > 5000000:
    tax = ((income - 5000000) * 0.35) + 1265000
    print(f"The tax amount you have to pay this year : {tax:.2f}")
elif income > 2000000:
    tax = ((income - 2000000) * 0.30) + 365000
    print(f"The tax amount you have to pay this year : {tax:.2f}")
elif income > 1000000:
    tax = ((income - 1000000) * 0.25) + 115000
    print(f"The tax amount you have to pay this year : {tax:.2f}")
elif income > 750000:
    tax = ((income - 750000) * 0.20) + 65000
    print(f"The tax amount you have to pay this year : {tax:.2f}")
elif income > 500000:
    tax = ((income - 500000) * 0.15) + 27500
    print(f"The tax amount you have to pay this year : {tax:.2f}")
elif income > 300000:
    tax = ((income - 300000) * 0.10) + 7500
    print(f"The tax amount you have to pay this year : {tax:.2f}")
elif income > 150000:
    tax = (income - 150000) * 0.05
    print(f"The tax amount you have to pay this year : {tax:.2f}")
else:
    print("The tax amount you have to pay this year : 0.00")