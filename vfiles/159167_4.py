money =float(input("Please enter your net income: "))

if money <0:
    print("asacacsa")
else:    
    if money <= 150000 :
        tax = 0.00
    elif money <= 300000:
            tax = (money - 150000) * 0.05
    elif money <= 500000:
            tax = ((money - 150000) * 0.10)+7500
    elif money <= 750000:
            tax = ((money - 150000) * 0.15)+27500
    elif money <= 1000000:
            tax = ((money - 750000) * 0.2)+65000
    elif money <= 2000000:
            tax = ((money - 1000000) * 0.25)+115000
    elif money <= 5000000:
            tax = ((money - 2000000) * 0.30)+365000
    else:
        tax = ((money - 5000000) * 0.35)+1265000
print(f"The tax amount you have to pay this year : {tax:.2f}")