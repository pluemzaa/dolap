net = float(input("Please enter your net income: "))

if net >= 0 and net <= 150000:
   tax = 0
elif net >= 150001 and net <= 300000:
   tax = (net-150000)*(5/100)
elif net >= 300001 and net <= 500000:
   tax = (net-300000)*(10/100)+7500
elif net >= 500001 and net <= 750000:
   tax = (net-500000)*(15/100)+27500
elif net >= 750001 and net <= 1000000:
   tax = (net-750000)*(20/100)+65000
elif net >= 1000001 and net <= 2000000:
   tax = (net-1000000)*(25/100)+115000
elif net >= 2000001 and net <= 5000000:
   tax = (net-2000000)*(30/100)+365000
elif net >5000000:
   tax = (net-5000000)*(35/100)+1265000

print (f"The tax amount you have to pay this year : {tax:.2f}")