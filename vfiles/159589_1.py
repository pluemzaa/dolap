cost = int(input("Please enter your net income: "))

if 0 < cost < 150000:
    print(f"The tax amount you have to pay this year : 0.00")
elif 150001 < cost < 300000:
    tex = (cost - 150000) * (5 / 100)
    print(f"The tax amount you have to pay this year : {tex:.2f}")
elif 300001 < cost < 500000:
    tex = ((cost - 300000) * (10 / 100)) + 7500
    print(f"The tax amount you have to pay this year : {tex:.2f}")
elif 500001 < cost < 750000:
    tex = ((cost - 500000) * (15 / 100)) + 27500
    print(f"The tax amount you have to pay this year : {tex:.2f}")
elif 750001 < cost < 1000000:
    tex = ((cost - 750000) * (20 / 100)) + 65000
    print(f"The tax amount you have to pay this year : {tex:.2f}")
elif 1000001 < cost < 2000000:
    tex = ((cost - 1000000) * (25 / 100)) + 115000
    print(f"The tax amount you have to pay this year : {tex:.2f}")
elif 2000001 < cost < 5000000:
    tex = ((cost - 2000000) * (30 / 100)) + 365000
    print(f"The tax amount you have to pay this year : {tex:.2f}")
elif 5000000 < cost:
    tex = ((cost - 5000000) * (35 / 100)) + 1265000
    print(f"The tax amount you have to pay this year : {tex:.2f}")