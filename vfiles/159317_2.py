Income = int(input("Please enter your net income: "))
Tax = float
I = int(Income)

if Income <= 150000 :
    Tax = 0
elif Income <= 300000 :
    Tax = (I - 150,000) * 0.05
elif Income <= 500000 :
    Tax = (I - 300,000) * 0.1 + 7500
elif Income <= 750000 :
    Tax = (I - 500,000) * 0.15 + 27500
elif Income <= 1000000 :
    Tax = (I - 750,000) * 0.2 + 65000
elif Income <= 2000000 :
    Tax = (I - 1,000,000) * 0.25 + 115000
elif Income <= 5000000 :
    Tax = (I - 2,000,000) * 0.3 + 365000
else :
    Tax = (I - 5,000,000) * 0.35 + 1265000

print ("The tax amount you have to pay this year : %.2f" %Tax)