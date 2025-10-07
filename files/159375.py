m = int(input('Please enter your net income: '))
if m >= 0 and m <= 150000:
    fee = 0
    print(f'The tax amount you have to pay this year :{fee:.2f}')
elif m >= 150001 and m <= 300000:
    fee = (m - 150000) * 0.05
    print(f'The tax amount you have to pay this year :{fee:.2f}')
elif m >= 300001 and m <= 500000:
    fee = ((m - 300000) * 0.1) + 7500
    print(f'The tax amount you have to pay this year :{fee:.2f}')
elif m >= 500001 and m <= 750000:
    fee = ((m - 500000) * 0.15) + 27500
    print(f'The tax amount you have to pay this year :{fee:.2f}')
elif m >= 750001 and m <= 1000000:
    fee = ((m - 750000) * 0.20) + 65000
    print(f'The tax amount you have to pay this year :{fee:.2f}')
elif m >= 1000001 and m <= 2000000:
    fee = ((m - 1000000) * 0.25) + 115000
    print(f'The tax amount you have to pay this year :{fee:.2f}')
elif m >= 2000001 and m < 5000000:
    fee = ((m - 2000000) * 0.30) + 365000
    print(f'The tax amount you have to pay this year :{fee:.2f}')
elif m >= 5000000:
    fee = ((m - 5000000) * 0.35) + 1265000
    print(f'The tax amount you have to pay this year :{fee:.2f}')