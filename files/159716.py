inc = float(input("Please enter your net income: "))
if 0 <= inc <= 150000:
    print(f"The tax amount you have to pay this year : {0:.2f}")
if 150001 <= inc <= 300000:
    print(f"The tax amount you have to pay this year : {(inc - 150000)*5/100:.2f}")
if 300001 <= inc <= 500000:
    print(f"The tax amount you have to pay this year : {((inc - 300000)*10/100)+7500:.2f}")
if 500001 <= inc <= 750000:
    print(f"The tax amount you have to pay this year : {((inc - 500000)*15/100)+27500:.2f}")
if 750001 <= inc <= 1000000:
    print(f"The tax amount you have to pay this year : {((inc - 750000)*20/100)+65000:.2f}")
if 1000001 <= inc <= 2000000:
    print(f"The tax amount you have to pay this year : {((inc - 1000000)*25/100)+115000:.2f}")
if 2000001 <= inc <= 5000000:
    print(f"The tax amount you have to pay this year : {((inc - 2000000)*30/100)+365000:.2f}")
if inc >= 5000000:
    print(f"The tax amount you have to pay this year : {((inc - 5000000)*35/100)+1265000:.2f}")