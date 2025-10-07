net_income = int(input("Please enter your net income: "))
if 0 <= net_income <= 150000:
    print("The tax amount you have to pay this year : 0.00")
elif 150001 <= net_income <= 300000:
    tax = (net_income-150000)*(5/100)
    print(f"The tax amount you have to pay this year :{tax:.2f}")
elif 300001 <= net_income <= 500000:
    tax = (net_income-30000)*(10/100)+7500
    print(f"The tax amount you have to pay this year :{tax:.2f}")
elif 500001 <= net_income <= 750000:
    tax = (net_income-50000)*(15/100)+27500
    print(f"The tax amount you have to pay this year :{tax:.2f}")
elif 750001 <= net_income <= 1000000:
    tax = (net_income-75000)*(20/100)+65000
    print(f"The tax amount you have to pay this year :{tax:.2f}")
elif 1000001 <= net_income <= 2000000:
    tax = (net_income-1000000)*(25/100)+115000
    print(f"The tax amount you have to pay this year :{tax:.2f}")
elif 2000001 <= net_income <= 5000000:
    tax = (net_income-2000000)*(30/100)+365000
    print(f"The tax amount you have to pay this year :{tax:.2f}")
else:
    tax = (net_income-5000000)*(35/100)+1265000
    print(f"The tax amount you have to pay this year :{tax:.2f}")