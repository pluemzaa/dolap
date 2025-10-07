x = int(input("Please enter your net income: "))
tax = ("The tax amount you have to pay this year : ")
z = 0
if x > 0 and x <= 150000:
    print("The tax amount you have to pay this year : 0.00")
elif x > 150000 and x <= 300000:
    z = (x-150000)*0.05
    print(f"The tax amount you have to pay this year : {z:.2f}")
elif x > 300001 and x <= 500000:
    z = ((x-300000)*0.10)+7500
    print(f"The tax amount you have to pay this year : {z:.2f}")
elif x > 500001 and x <= 750000:
    z = ((x-500000)*0.15)+27500
    print(f"The tax amount you have to pay this year : {z:.2f}")
elif x > 751000 and x <= 1000000:
    z = ((x-750000)*0.20)+65000
    print(f"The tax amount you have to pay this year : {z:.2f}")
elif x > 1000001 and x <= 2000000:
    z = ((x-1000000)*0.25)+115000
    print(f"The tax amount you have to pay this year : {z:.2f}")
elif x > 2000001 and x <= 5000000:
    z = ((x-2000000)*0.30)+365000
    print(f"The tax amount you have to pay this year : {z:.2f}")
elif x > 5000000:
    z = ((x-5000000)*0.35)+1265000
    print(f"The tax amount you have to pay this year : {z:.2f}")