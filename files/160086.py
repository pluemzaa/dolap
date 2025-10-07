money = float(input("Please enter your net income: "))

if 0 <= money <= 150000:
    print("The tax amount you have to pay this year : 0.00")
elif 150001 <= money <= 300000:
    tax = (money - 150000) * 0.05
    print(f"The tax amount you have to pay this year : {tax:.2f}")
elif 300001 <= money <= 500000:
    tax = ((money - 300000) * 0.10) + 7500
    print(f"The tax amount you have to pay this year : {tax:.2f}")
elif 500001 <= money <= 750000:
    tax = ((money - 500000) * 0.15) + 27500
    print(f"The tax amount you have to pay this year : {tax:.2f}")
elif 750001 <= money <= 1000000:
    tax = ((money - 750000) * 0.20) + 65000
    print(f"The tax amount you have to pay this year : {tax:.2f}")
elif 1000001 <= money <= 2000000:
    tax = ((money - 1000000) * 0.25) + 115000
    print(f"The tax amount you have to pay this year : {tax:.2f}")
elif 2000001 <= money <= 5000000:
    tax = ((money - 2000000) * 0.30) + 365000
    print(f"The tax amount you have to pay this year : {tax:.2f}")
elif money > 5000000 :
    tax = ((money - 5000000) * 0.35) + 1265000
    print(f"The tax amount you have to pay this year : {tax:.2f}")