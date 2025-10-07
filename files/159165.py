i = int(input("Please enter your net income: "))
if i < 150000 and i > 0 :
    tax = 0
elif i > 150000 and i <= 300000 :
    tax = (i - 150000) * 0.05
elif i > 300000 and i <= 500000 :
    tax = ((i - 300000) * 0.10)+7500
elif i > 500000 and i <= 750000 :
    tax = ((i - 500000) * 0.15)+27500
elif i > 750000 and i <= 1000000 :
    tax = ((i - 750000) * 0.2)+65000
elif i > 1000000 and i <= 2000000 :
    tax = ((i - 1000000) * 0.25)+115000
elif i > 2000000 and i <= 5000000 :
    tax = ((i - 2000000) * 0.3)+365000
elif i > 5000000 :
    tax = ((i - 5000000) * 0.35)+1265000
print (f"The tax amount you have to pay this year : {tax:.2f}")