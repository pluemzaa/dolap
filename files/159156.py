income = float(input("Please enter your net income: "))

if income>0:
    if income <= 150000:
        tax = 0
    elif income <= 300000:
        tax = ((income-150000)*5)/100
    elif income <= 500000:
        tax = (((income-300000)*10)/100)+7500
    elif income <= 750000:
        tax = (((income-500000)*15)/100)+27500
    elif income <= 1000000:
        tax = (((income-750000)*20)/100)+65000
    elif income <= 2000000:
        tax = (((income-1000000)*25)/100)+115000
    elif income <= 5000000:
        tax = (((income-2000000)*30)/100)+365000
    else:
        tax = (((income-5000000)*35)/100)+1265000
    
    print(f"The tax amount you have to pay this year : {tax:.2f}")