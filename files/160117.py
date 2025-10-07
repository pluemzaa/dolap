c = int(input("Please enter your net income: "))

if  c <= 150000:
    i = 0
    print(f"The tax amount you have to pay this year : {i:.2f}")

elif c <= 300000:
    i = (c - 150000) * 5/100
    print(f"The tax amount you have to pay this year : {i:.2f} ")
elif c <= 500000:
    i = (c - 300000) * 10/100  + 7500
    print(f"The tax amount you have to pay this year : {i:.2f} ")
elif c <= 750000:
    i = (c - 500000) * 15/100  + 27500
    print(f"The tax amount you have to pay this year : {i:.2f} ")
elif c <= 1000000:
    i = (c - 750000) * 20/100  + 65000
    print(f"The tax amount you have to pay this year : {i:.2f} ")
elif c <= 2000000:
    i = (c - 1000000) * 25/100  + 115000
    print(f"The tax amount you have to pay this year : {i:.2f} ")
elif c <= 5000000:
    i = (c - 2000000) * 30/100  + 365000
    print(f"The tax amount you have to pay this year : {i:.2f} ")

else:
    i = (c - 5000000) * 35/100  + 1265000
    print(f"The tax amount you have to pay this year : {i:.2f}")