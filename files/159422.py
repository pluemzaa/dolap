m = float(input("Please enter your net income: "))
tax = 0
if m >= 0 and m <=150000:
    print(f"The tax amount you have to pay this year : {tax:.2f}")
elif m >= 150001 and m <=300000:
    tax = (m-150000)*0.05
    print(f"The tax amount you have to pay this year : {tax:.2f}")
elif m >= 300001 and m <=500000:
    tax = ((m-300000)*0.1)+7500
    print(f"The tax amount you have to pay this year : {tax:.2f}")
elif m >= 500001 and m <=750000:
    tax = ((m-500000)*0.15)+27500
    print(f"The tax amount you have to pay this year : {tax:.2f}")
elif m >= 750001 and m <=1000000:
    tax = ((m-750000)*0.2)+65000
    print(f"The tax amount you have to pay this year : {tax:.2f}")
elif m >= 1000001 and m <=2000000:
    tax = ((m-1000000)*0.25)+115000
    print(f"The tax amount you have to pay this year : {tax:.2f}")
elif m >= 2000001 and m <=5000000:
    tax = ((m-2000000)*0.3)+365000
    print(f"The tax amount you have to pay this year : {tax:.2f}")
elif m >= 5000001:
    tax = ((m-5000000)*0.35)+1265000
    print(f"The tax amount you have to pay this year : {tax:.2f}")