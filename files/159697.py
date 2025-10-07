money=int(input("Please enter your net income: "))
vat=0
if  money>=0 and money<=150000 :
    vat=0
if money>=150001 and money<= 300000 :
    vat=(money-150000)*0.05
if money>=300001 and money<= 500000 :
    vat=((money-300000)*0.1)+7500
if money>=500001 and money<= 750000 :
    vat=((money-50000)*0.15)+27500
if money>=750001 and money<= 1000000 :
    vat=((money-750000)*0.20)+65000
if money>=1000001 and money<= 2000000 :
    vat=((money-1000000)*0.25)+115000
if money>=2000001 and money<= 5000000 :
    vat=((money-2000000)*0.30)+365000
if money>=5000001 :
    vat=((money-5000000)*0.35)+1265000
    print(f"The tax amount you have to pay this year : {vat:.2f}")
else:
    print(f"The tax amount you have to pay this year : {vat:.2f}")