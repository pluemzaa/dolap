net_income = float(input("Please enter your net income: "))
tax = 0

if net_income <= 150000:
    print(f"The tax amount you have to pay this year : {tax:.2f}")
elif net_income <= 300000:
        tax = (net_income - 150000) * 5/100 
        print(f"The tax amount you have to pay this year : {tax:.2f}")
elif net_income <= 500000:
        tax = (net_income - 300000) * 10/100 + 7500
        print(f"The tax amount you have to pay this year : {tax:.2f}")
elif net_income <= 750000:
        tax = (net_income - 500000) * 15/100 + 27500
        print(f"The tax amount you have to pay this year : {tax:.2f}")
elif net_income <= 1000000:
        tax = (net_income - 750000) * 20/100 + 65000
        print(f"The tax amount you have to pay this year : {tax:.2f}")
elif net_income <= 2000000:
        tax = (net_income - 1000000) * 25/100 + 115000
        print(f"The tax amount you have to pay this year : {tax:.2f}")
elif net_income <= 5000000:
        tax = (net_income - 2000000) * 30/100 + 365000
        print(f"The tax amount you have to pay this year : {tax:.2f}")
elif net_income > 5000000:
        tax = (net_income - 5000000) * 35/100 + 1265000
        print(f"The tax amount you have to pay this year : {tax:.2f}")      
else:
    print(f"The tax amount you have to pay this year : {tax:.2f}")