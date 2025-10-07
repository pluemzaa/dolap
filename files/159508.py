incor = float(input("Please enter your net income:"))

if incor < 0:
        print("Invaild input: Income cannot be negative.")
else:
    tax = 0.0
    
    if incor <= 150000:
        tax = 0
    elif incor <= 300000:
        tax = (incor - 150000) * 0.05
    elif incor <= 500000:
        tax = ((incor - 300000) * 0.10) + 7500
    elif incor <= 750000:
        tax = ((incor - 500000) * 0.15) + 27500
    elif incor <= 1000000:
        tax = ((incor - 750000) * 0.20) + 65000
    elif incor <= 2000000:
        tax = ((incor - 1000000) * 0.25) + 115000
    elif incor <= 5000000:
        tax = ((incor - 2000000) * 0.30) + 365000
    else:
        tax = ((incor - 5000000) * 0.35) + 1265000
    print(f"The tax amount you have to pay this year : {tax:.2f}")