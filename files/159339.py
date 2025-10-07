i = float(input("Please enter your net income: "))

if  i >= 0:
    if i <= 150000:
        tax = 0
    elif i <= 300000:
        tax = (((i-150000)*5)/100)
    elif i <= 500000:
        tax = (((i-300000)*10)/100)+7500
    elif i <= 750000:
        tax = (((i-500000)*15)/100)+27000
    elif i <= 1000000:
        tax = (((i-750000)*20)/100)+65000
    elif i <= 2000000:
        tax = (((i-1000000)*25)/100)+115000
    elif i <= 5000000:
        tax = (((i-2000000)*30)/100)+365000
    else:
        tax = (((i-5000000)*35)/100)+1265000

    print (f"The tax amount you have to pay this year : {tax:.2f}")