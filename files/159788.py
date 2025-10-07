ni = int(input("Please enter your net income: "))
if ni >= 0 and ni <= 150000:
  t = 0
elif ni >= 150001 and ni <= 300000:
  t = (ni - 150000)* 0.05
elif ni >= 300001 and ni <= 500000:
  t = ((ni - 300000)* 0.10) + 7500
elif ni >= 500001 and ni <= 750000:
  t = ((ni - 500000)* 0.15) + 27500
elif ni >= 750001 and ni <= 1000000:
  t = ((ni - 750000)* 0.20) + 65000
elif ni >= 1000001  and ni <= 2000000:
  t = ((ni - 1000000)* 0.25) + 115000
elif ni >= 2000001  and ni <= 5000000:
  t = ((ni - 2000000)* 0.30) + 365000
else:
  t = ((ni - 5000000)* 0.35) + 1265000
print(f"The tax amount you have to pay this year : {t:.2f}")