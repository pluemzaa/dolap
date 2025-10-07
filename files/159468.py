money = int(input("Please enter your net income: "))

if money >= 0:
    if money >=0 and money <= 150000:
        print("The tax amount you have to pay this year : 0.00")
    elif money >= 150001 and money <= 300000 :
        tax = (money - 150000)*0.05
        print(f"The tax amount you have to pay this year : {tax:.2f}")
    elif money >= 300001 and money <= 500000:
        tax = (money - 300000)*0.10 + 7500
        print(f"The tax amount you have to pay this year : {tax:.2f}")
    elif money >=500001 and money <= 750000:
        tax = (money - 500000)*0.15 + 27500
        print(f"The tax amount you have to pay this year : {tax:.2f}")
    elif money >= 750001 and money <= 1000000:
        tax = (money - 750000)*0.20 + 65000
        print(f"The tax amount you have to pay this year : {tax:.2f}")
    elif money >= 1000001 and money <= 2000000:
        tax = (money - 1000000)*0.25 + 115000
        print(f"The tax amount you have to pay this year : {tax:.2f}")
    elif money >= 2000001 and money <= 5000000:
        tax = (money - 2000000)*0.30 + 365000
        print(f"The tax amount you have to pay this year : {tax:.2f}")
    elif money >= 5000001:
        tax = (money - 5000000)*0.35 + 1265000
        print(f"The tax amount you have to pay this year : {tax:.2f}")