N = float(input("Please enter your net income:"))
if N >= 0 and N <= 150000:
    tax = 0
    print(f"The tax amount you have to pay this year : {tax:.2f}")
elif N >= 150001 and N <= 300000:
    tax = (N-150000)*0.05
    print(f"The tax amount you have to pay this year : {tax:.2f}")
elif N >= 300001 and N <= 500000:
    tax = (N-300000)*0.10 + 7500
    print(f"The tax amount you have to pay this year : {tax:.2f}")
elif N >= 500001 and N <= 750000:
    tax = (N-500000)*0.15 + 27500
    print(f"The tax amount you have to pay this year : {tax:.2f}")
elif N >= 750001 and N <= 1000000:
    tax = (N-750000)*0.20 + 65000
    print(f"The tax amount you have to pay this year : {tax:.2f}")
elif N >= 1000001 and N <= 2000000:
    tax = (N-1000000)*0.25 + 115000
    print(f"The tax amount you have to pay this year : {tax:.2f}")
elif N >= 2000001 and N <= 5000000:
    tax = (N-2000000)*0.30 + 365000
    print(f"The tax amount you have to pay this year : {tax:.2f}")
else:
    tax = (N-5000000)*0.35 + 1265000
    print(f"The tax amount you have to pay this year : {tax:.2f}")