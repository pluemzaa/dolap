Income = int(input("Please enter your net income: "))
Tax = float

if Income <= 150000 :
    Tax = 0
elif Income <= 300000 :
    Tax = (Income - 150,000) * 0.05
elif Income <= 500000 :
    Tax = [ (Income - 300,000) * 0.1 ] + 7,500
elif Income <= 750000 :
    Tax = [ (Income - 500,000) * 0.15 ] + 27,500
elif Income <= 1000000 :
    Tax = [ (Income - 750,000) * 0.2 ] + 65,000
elif Income <= 2000000 :
    Tax = [ (Income - 1,000,000) * 0.25 ] + 115,000
elif Income <= 5000000 :
    Tax = [ (Income - 2,000,000) * 0.3 ] + 365,000
else :
    Tax = [ (Income - 5,000,000) * 0.35 ] + 1,265,000

print ("The tax amount you have to pay this year : %.2f" %Tax)