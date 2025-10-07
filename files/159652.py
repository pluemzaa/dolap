net = int(input("Please enter your net income: "))
if net >= 0 and net <= 150000 :
    tax = net*0
if net >= 150001 and net <= 300000 :
    tax = (net-150000)*0.05
if net >= 300001 and net <= 500000 :
    tax = ((net-300000)*0.10)+7500
if net >= 500001 and net <= 750000 :
    tax = ((net-500000)*0.15)+27500
if net >= 750001 and net <= 1000000 :
    tax = ((net-750000)*0.20)+65000
if net >= 1000001 and net <= 2000000 :
    tax = ((net-1000000)*0.25)+115000
if net >= 2000001 and net <= 5000000 :
    tax = ((net-2000000)*0.30)+365000
if net > 5000000 :
    tax = ((net-5000000)*0.35)+1265000
    
print(f"The tax amount you have to pay this year : {tax:.2f}")