income = int(input("Please enter your net income:"))
if income <= 150000:
    print("The tax amount you have to pay this year : 0.00")
elif income <=300000:
    price = (income - 150000) * 0.05
    print("The tax amount you have to pay this year : %.2f" % price)
elif income <= 500000:
    price = ((income - 300000) * 0.1) + 7500
    print("The tax amount you have to pay this year : %.2f" % price)
elif income <= 750000:
    price = ((income - 50000) * 0.15) + 27500
elif income <= 1000000:
    price = ((income - 750000) * 0.20) + 65000
    print("The tax amount you have to pay this year : %.2f" % price)
elif income <= 2000000:
    price = ((income - 1000000) * 0.25) + 115000
    print("The tax amount you have to pay this year : %.2f" % price)
elif income <= 5000000:
    price = ((income - 2000000) * 0.30) + 365000
    print("The tax amount you have to pay this year : %.2f" % price)
else:
    price = ((income - 5000000) * 0.35) + 1265000
    print("The tax amount you have to pay this year : %.2f" % price)