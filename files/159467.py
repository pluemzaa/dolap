inc = float(input("Please enter your net income: "))
re = 0
if inc >= 0 and inc <= 150000:
    print(f"The tax amount you have to pay this year : {re:.2f}")
if inc >= 150001 and inc <= 300000:
    re = (inc - 150000) * 0.05
    print(f"The tax amount you have to pay this year : {re:.2f}")
if inc >= 300001 and inc <= 500000:
    re = ((inc - 300000)* 0.10) + 7500
    print(f"The tax amount you have to pay this year : {re:.2f}")
if inc >= 500001 and inc <= 750000:
    re = ((inc - 500000) * 0.15) + 27500
    print(f"The tax amount you have to pay this year : {re:.2f}")
if inc >= 750001 and inc <= 1000000:
    re = ((inc - 750000) * 0.20) + 65000
    print(f"The tax amount you have to pay this year : {re:.2f}")
if inc >= 1000001 and inc <= 2000000:
    re = ((inc - 1000000) * 0.25) + 115000
    print(f"The tax amount you have to pay this year : {re:.2f}")  
if inc >= 2000001 and inc <= 5000000:
    re = ((inc - 2000000) * 0.30) + 365000
    print(f"The tax amount you have to pay this year : {re:.2f}")
if inc > 5000000:
    re = ((inc - 5000000) * 0.35) + 1265000
    print(f"The tax amount you have to pay this year : {re:.2f}")