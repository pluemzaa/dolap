tax = float(input("Please enter your net income:"))

if tax <= 150000:
    print("The tax amount you have to pay this year : 0.00")
elif tax <= 300000:
    print("The tax amount you have to pay this year : %.2f" %((tax - 150000)*0.05))
elif tax <= 500000:
    print("The tax amount you have to pay this year : %.2f" %(((tax - 300000)*0.10)+7500))
elif tax <= 750000:
    print("The tax amount you have to pay this year : %.2f" %(((tax - 500000)*0.15)+27500))
elif tax <= 1000000:
    print("The tax amount you have to pay this year : %.2f" %(((tax - 750000)*0.20)+65000))
elif tax <= 2000000:
    print("The tax amount you have to pay this year : %.2f" %(((tax - 1000000)*0.25)+115000))
elif tax <= 5000000:
    print("The tax amount you have to pay this year : %.2f" %(((tax - 2000000)*0.30)+365000))
else:
    print("The tax amount you have to pay this year : %.2f" %(((tax - 5000000)*0.35)+1265000))