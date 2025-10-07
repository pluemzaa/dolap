income = float(input("Please enter your net income: "))
if income >= 0 and income <= 150000 :
    tax = 0
if income >= 150001 and income <= 300000 :
    tax = (income-150000)*0.05
if income >= 300001 and income <= 500000 :
    tax = ((income-300000)*0.10)+7500
if income >= 500001 and income <= 750000 :
    tax = ((income-500000)*0.15)+27500
if income >= 750001 and income <= 1000000 :
    tax = ((income-750000)*0.20)+65000
if income >= 1000001 and income <= 2000000 :
    tax = ((income-1000000)*0.25)+115000
if income >= 2000001 and income <= 5000000 :
    tax = ((income-2000000)*0.30)+365000
if income > 5000000 :
    tax = ((income-5000000)*0.35)+1265000
print(f"The tax amount you have to pay this year : {tax:.2f}")