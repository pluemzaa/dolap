x = int(input("Please enter your net income: "))
y = 0
if x >150000 and x <= 300000:
    y = (x - 150000) * 0.5
elif x > 300000 and x <= 500000:
    y = ((x - 300000) * 0.1)+ 7500
elif x > 500000 and x <= 750000:
    y = ((x - 500000) * 0.15) + 27500
elif x > 750000 and x <= 1000000:
    y = ((x - 750000) * 0.2) + 65000
elif x > 1000000 and x <= 2000000:
    y = ((x - 1000000) * 0.25) + 115000
elif x > 2000000 and x <= 5000000:
    y = ((x - 2000000) * 0.3) + 365000   
elif x > 5000000:
    y = ((x - 5000000) * 0.35) + 1265000                           
else :
     y = x*0
print(f"The tax amount you have to pay this year : {y:.2f} Baht")