net_income = float(input("Please enter your net income:"))

if net_income <= 0 or net_income <= 150000:
    print("The tax amount you have to pay this year : 0.00")
elif net_income >= 150001 and net_income <= 300000:
    vat = (net_income - 150000 ) * 0.05
    print(f"The tax amount you have to pay this year :{vat:.2f}")
elif net_income >= 300001 and net_income <= 500000:
    vat = ((net_income - 300000)* 0.10) + 7500
    print(f"The tax amount you have to pay this year :{vat:.2f}")
elif net_income >= 500001 and net_income <= 750000:
    vat = ((net_income - 750000)* 0.15) + 27500
    print(f"The tax amount you have to pay this year :{vat:.2f}")
elif net_income >= 750001 and net_income <= 1000000:
    vat = ((net_income - 750000)* 0.20) + 65000
    print(f"The tax amount you have to pay this year :{vat:.2f}")
elif net_income >= 1000001 and net_income <= 2000000:
    vat = ((net_income - 1000000)* 0.25) + 115000
    print(f"The tax amount you have to pay this year :{vat:.2f}")
elif net_income >= 2000001 and net_income <= 5000000:
    vat = ((net_income - 2000000)* 0.30) + 365000
    print(f"The tax amount you have to pay this year :{vat:.2f}")
else:
    vat = ((net_income - 5000000)* 0.35) + 1265000
    print(f"The tax amount you have to pay this year :{vat: .2f}")