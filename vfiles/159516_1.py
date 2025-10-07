s = float(input("Please enter your net income: "))
P = 0
if  s <= 150000:
    p = 0
    print(f"The tax amount you have to pay this year :{p :.2f}")
elif s <= 300000:
    p = (s-150000)*0.05
    print(f"The tax amount you have to pay this year :{p :.2f}")
elif s <= 500000:
    p = ((s - 300000)*0.10)+7500
    print(f"The tax amount you have to pay this year :{p :.2f}")
elif s <= 750000:
    p = ((s - 500000)*0.15)+27500
    print(f"The tax amount you have to pay this year :{p :.2f}")
elif s <= 1000000:
    p = ((s - 750000)*0.20)+65000
    print(f"The tax amount you have to pay this year :{p :.2f}")
elif s <= 2000000:
    p = ((s - 1000000)*0.25)+11500
    print(f"The tax amount you have to pay this year :{p :.2f}")
elif s <= 5000000:
    p = ((s- 2000000)*0.30)+365000
    print(f"The tax amount you have to pay this year :{p :.2f}")
elif s > 5000000:
    p = ((s-5000000)*0.35)+1265000
    print(f"The tax amount you have to pay this year :{p :.2f}")