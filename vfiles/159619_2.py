net_income = float(input("Please enter your net income: "))

if net_income >= 0 and net_income <= 150000:
    print("The tax amount you have to pay this year : 0.00")
elif net_income >= 150001 and net_income <= 300000:
    tax_1 = (net_income - 150000) * 5/100
    print("The tax amount you have to pay this year : %.2f"%tax_1)
elif net_income >= 300001 and net_income <= 500000:
    tax_2 = ((net_income - 300000) * 10/100) + 7500
    print("The tax amount you have to pay this year : %.2f"%tax_2)
elif net_income >= 500001 and net_income <=750000:
    tax_3 = ((net_income - 500000) * 15/100) + 27500
    print("The tax amount you have to pay this year : %.2f"%tax_3)
elif net_income >= 750001 and net_income <= 1000000:
    tax_4 = ((net_income - 750000) * 20/100) + 65000
    print("The tax amount you have to pay this year : %.2f"%tax_4)
elif net_income >= 1000001 and net_income <= 2000000:
    tax_5 = ((net_income - 1000000) * 25/100) + 11500
    print("The tax amount you have to pay this year : %.2f"%tax_5)
elif net_income >= 2000001 and net_income <= 5000000:
    tax_6 = ((net_income - 2000000) * 30/100) +365000
    print("The tax amount you have to pay this year : %.2f"%tax_6)
elif net_income > 5000000:
    tax_7 = ((net_income - 5000000) * 35/100) + 1265000
    print("The tax amount you have to pay this year : %.2f"%tax_7)