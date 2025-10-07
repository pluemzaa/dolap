inc = float(input("Please enter your net income: "))

if inc < 0:
        print("Invalid input: Income cannot be negative.")
else:
    tax = 0.0
        
    if inc <= 150000:
        tax = 0
    elif inc <= 300000:
        tax = (inc - 150000) * 0.05
    elif inc <= 500000:
        tax = ((inc - 300000) * 0.10) + 7500
    elif inc <= 750000:
        tax = ((inc - 500000) * 0.15) + 27500
    elif inc <= 1000000:
        tax = ((inc - 750000) * 0.20) + 65000
    elif inc <= 2000000:
        tax = ((inc - 1000000) * 0.25) + 115000
    elif inc <= 5000000:
        tax = ((inc - 2000000) * 0.30) + 365000
    else:
        tax = ((inc - 5000000) * 0.35) + 1265000
    print(f"The tax amount you have to pay this year : {tax:.2f}")