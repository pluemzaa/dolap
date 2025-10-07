net = int(input("Please enter your net income:"))
tt = 0
if net >= 0 and net <= 150000:
    print(f"The tax amount you have to pay this year :{tt : .2f}")
elif net >= 150001 and net <= 300000:
    tax = 5 / 100
    tax = float(tax)
    t = (net - 150000) * tax
    print(f"The tax amount you have to pay this year :{t : .2f}")
elif net >= 300001 and net <= 500000:
    tax = 10 / 100
    tax = float(tax)
    t = ((net - 300000) * tax) + 7500
    print(f"The tax amount you have to pay this year :{t : .2f}")
elif net >= 500001 and net <= 750000:
    tax = 15 / 100
    tax = float(tax)
    t = ((net - 500000) * tax) + 27500
    print(f"The tax amount you have to pay this year :{t : .2f}")
elif net >= 750001 and net <= 1000000:
    tax = 20 / 100
    tax = float(tax)
    t = ((net - 750000) * tax) + 65000
    print(f"The tax amount you have to pay this year :{t : .2f}")
elif net >= 1000001 and net <= 2000000:
    tax = 25 / 100
    tax = float(tax)
    t = ((net - 1000000) * tax) + 115000
    print(f"The tax amount you have to pay this year :{t : .2f}")
elif net >= 2000001 and net <= 5000000:
    tax = 30 / 100
    tax = float(tax)
    t = ((net - 2000000) * tax) + 365000
    print(f"The tax amount you have to pay this year :{t : .2f}")
elif net > 5000000:
    tax = 35 / 100
    tax = float(tax)
    t = ((net - 5000000) * tax) + 1265000
    print(f"The tax amount you have to pay this year :{t : .2f}")
else:
    pass