netincome = float(input('Please enter your net income: '))
if netincome >= 0 and netincome <= 150000:
    print('The tax amount you have to pay this year : 0.00')
if netincome >= 150001 and netincome <= 300000:
    a = (netincome - 150000)*5/100
    print('The tax amount you have to pay this year : %.2f'%a)
if netincome >= 300001 and netincome <= 500000:
    b = ((netincome - 300000)*10/100)+7500
    print('The tax amount you have to pay this year : %.2f'%b)
if netincome >= 500001 and netincome <= 750000:
    c = ((netincome - 500000)*15/100)+27500
    print('The tax amount you have to pay this year : %.2f'%c)
if netincome >= 750001 and netincome <= 1000000:
    d = ((netincome - 750000)*20/100)+65000
    print('The tax amount you have to pay this year : %.2f'%d)
if netincome >= 1000001 and netincome <= 2000000:
    e = ((netincome - 1000000)*25/100)+115000
    print('The tax amount you have to pay this year : %.2f'%e)
if netincome >= 2000001 and netincome <= 5000000:
    f = ((netincome - 2000000)*30/100)+365000
    print('The tax amount you have to pay this year : %.2f'%f)
if netincome > 5000000:
    g = ((netincome - 5000000)*35/100)+1265000
    print('The tax amount you have to pay this year : %.2f'%g)