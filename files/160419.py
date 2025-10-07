net_income = int(input("Please enter your net income: "))
tex = 0
if 0 < net_income < 150000:
    tex = 0 
    print(f"The tax amount you have to pay this year :{tex:.2f} ")
elif 150001 <= net_income <= 300000:
    tex = (net_income - 150000) * 0.05
    print(f"The tax amount you have to pay this year :{tex:.2f} ")
elif 300001 <= net_income <= 500000:
    tex = ((net_income - 300000) * 0.1)+7500
    print(f"The tax amount you have to pay this year :{tex:.2f} ")
elif 500001 <= net_income <= 750000:
    tex = ((net_income - 500000) * 0.15) + 27500
    print(f"The tax amount you have to pay this year :{tex:.2f} ")
elif 750001 <= net_income <= 1000000 :
    tex = ((net_income - 750000) * 0.20) + 65000 
    print(f"The tax amount you have to pay this year :{tex:.2f} ")
elif 1000001 <= net_income <= 2000000:
    tex = ((net_income - 1000000) * 0.25) + 115000
    print(f"The tax amount you have to pay this year :{tex:.2f} ")
elif  2000001 <= net_income <= 5000000 :
    tex = ((net_income - 2000000) * 0.30) + 365000
    print(f"The tax amount you have to pay this year :{tex:.2f} ")
elif 5000000 <= net_income:
    tex = ((net_income - 5000000) * 0.35 ) + 1265000
    print(f"The tax amount you have to pay this year :{tex:.2f} ")