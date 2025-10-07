net_income = int(input("Please enter your net income: "))
if net_income <=150000:
    text = 0
elif net_income <=300000:
    text = (net_income-150000)*0.05
elif net_income <=500000:
    text = ((net_income-300000)*0.10)+7500
elif net_income <=750000:
    text = ((net_income-500000)*0.15)+27500
elif net_income <=1000000:
    text = ((net_income-750000)*0.20)+65000
elif net_income <=2000000:
    text = ((net_income-1000000)*0.25)+115000
elif net_income <=5000000:
    text = ((net_income-2000000)*0.30)+365000
else:
    text = ((net_income-5000000)*0.35)+1265000
print(f"The tax amount you have to pay this year : {text:.2f}")