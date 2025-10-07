n = float(input("Please enter your net income: "))
if n > 5000000:
    print(f"The tax amount you have to pay this year : {((n - 5000000)*(35/100))+1265000:.2f}")
elif n >= 2000001:
    print(f"The tax amount you have to pay this year : {((n - 2000000)*(30/100))+365000:.2f}")
elif n >= 1000001:
    print(f"The tax amount you have to pay this year : {((n - 1000000)*(25/100))+115000:.2f}")
elif n >= 750001:
    print(f"The tax amount you have to pay this year : {((n - 750000)*(20/100))+65000:.2f}")
elif n >= 500001:
    print(f"The tax amount you have to pay this year : {((n - 500000)*(15/100))+27500:.2f}")
elif n >= 300001:
    print(f"The tax amount you have to pay this year : {((n - 300000)*(10/100))+7500:.2f}")   
elif n >= 150001:
    print(f"The tax amount you have to pay this year : {(n - 150000)*(5/100):.2f}")
else:
    print("The tax amount you have to pay this year : 0.00")