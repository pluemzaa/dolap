m = int(input("Please enter your net income: "))
if m <= 150000 :
    print(f'The tax amount you have to pay this year: {(0):.2f}')
elif m <= 300000 :
    print(f'The tax amount you have to pay this year: {((m-150000)*5/100):.2f}')
elif m <= 500000 :
    print(f'The tax amount you have to pay this year: {(((m-300000)*10/100)+7500):.2f}')
elif m <= 750000 :
    print(f'The tax amount you have to pay this year: {(((m-500000)*15/100)+27500):.2f}')
elif m <= 1000000 :
    print(f'The tax amount you have to pay this year: {(((m-750000)*20/100)+65000):.2f}')
elif m <= 2000000 :
    print(f'The tax amount you have to pay this year: {(((m-1000000)*25/100)+115000):.2f}')
elif m <= 5000000 :
    print(f'The tax amount you have to pay this year: {(((m-2000000)*30/100)+365000):.2f}')
elif m > 5000000 :
    print(f'The tax amount you have to pay this year: {(((m-5000000)*35/100)+1265000):.2f}')