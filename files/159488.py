net = int(input("Please enter your net income: "))
tax = float(0)

if 0 <= net <= 150000 :
    print("The tax amount you have to pay this year : %.2f" %tax)
elif 150001 <= net <= 300000 :
    tax = (net-150000)*0.05
    print("The tax amount you have to pay this year : %.2f" %tax)
elif 300001 <= net <= 500000 :
    tax = ((net-300000)*0.1) + 7500
    print("The tax amount you have to pay this year : %.2f" %tax)
elif 500001 <= net <= 750000 :
    tax = ((net-500000)*0.15) + 27500
    print("The tax amount you have to pay this year : %.2f" %tax)
elif 750001 <= net <= 1000000 :
    tax = ((net-750000)*0.2) + 65000
    print("The tax amount you have to pay this year : %.2f" %tax)
elif 1000001 <= net <= 2000000 :
    tax = ((net-1000000)*0.25) + 115000
    print("The tax amount you have to pay this year : %.2f" %tax)
elif 2000001 <= net <= 5000000 :
    tax = ((net-2000000)*0.3) + 365000
    print("The tax amount you have to pay this year : %.2f" %tax)
elif net > 5000000 :
    tax = ((net-5000000)*0.35) + 1265000
    print("The tax amount you have to pay this year : %.2f" %tax)