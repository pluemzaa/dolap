income=float(input('Please enter your net income: '))

if income <= 150000:
    print('The tax amount you have to pay this year : 0.00')
if income >=15001 and income<= 300000 :
    print(f'The tax amount you have to pay this year : {(income-150000)*0.05:.2f}')
if income >=300001  and income<= 500000 :
    print(f'The tax amount you have to pay this year : {((income-300000)*0.10)+7500:.2f}')
if income >=500001 and income<= 750000 :
    print(f'The tax amount you have to pay this year : {((income-500000)*0.15)+27500:.2f}')
if income >=750001 and income<= 1000000 :
    print(f'The tax amount you have to pay this year : {((income-750000)*0.20)+65000:.2f}')
if income >=1000001 and income<= 2000000 :
    print(f'The tax amount you have to pay this year : {((income-1000000)*0.25)+115000:.2f}')
if income >=2000001 and income<= 5000000 :
    print(f'The tax amount you have to pay this year : {((income-2000000)*0.30)+365000:.2f}')
if income >5000000 :
    print(f'The tax amount you have to pay this year : {((income-5000000)*0.35)+1265000:.2f}')