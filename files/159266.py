money = float(input("Please enter your net income: "))

if money >=0 and money <= 150000:
    loan = money * 0

elif money >= 150001 and money <= 300000 :
    loan = (money - 150000) * (5/100)

elif money >= 300001 and money <= 500000:
    loan = (money - 300000) * (10/100) +7500

elif money >=500001 and money <= 750000:
    loan = (money - 500000) * (15/100) + 27500

elif money >= 750001 and money <= 1000000:
    loan = (money - 750000) * (20/100) + 65000

elif money >= 1000001 and money <= 2000000:
    loan = (money - 1000000) * (25/100) + 115000

elif money >= 2000001 and money <= 5000000:
    loan = (money - 2000000) * (30/100) + 365000
elif money >= 5000001:
    loan = (money - 5000000) * (35/100) + 1265000

print(f"The tax amount you have to pay this year : {loan:.2f}")