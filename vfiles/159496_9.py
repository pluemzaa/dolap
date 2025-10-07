n = float(input("Please enter your net income: "))
if n < 150000:
    print("The tax amount you have to pay this year : 0.00")
elif n <= 300000:
    print(f"The tax amount you have to pay this year : {(n-150000)*0.05:.2f}:")
elif n <= 500000:
    print(f"The tax amount you have to pay this year : {(n-300000)*0.1+7500:.2f}")
elif n <= 750000:
    print(f"The tax amount you have to pay this year : {(n-500000)*0.15+27500:.2f}")
elif n <= 1000000:
    print(f"The tax amount you have to pay this year : {(n-750000)*0.2+65000:.2f}")
elif n <= 2000000:
    print(f"The tax amount you have to pay this year : {(n-1000000)*0.25+115000:.2f}")
elif n <= 5000000:
    print(f"The tax amount you have to pay this year : {(n-2000000)*0.3+365000:.2f}")
elif n > 5000000:
    print(f"The tax amount you have to pay this year : {(n-5000000)*0.35+1265000:.2f}")