Member = input('Membership (y/n) : ')
Total = int(input('Total amount : '))

Total_Discount = 0

if Member == 'y':
    if Total >= 1000:
        Total_Discount = Total * 0.20
        print(f'Discount : {Total_Discount:.2f}')
        Final_price = Total-Total_Discount
        print (f'Final Amount to Pay : {Final_price:.2f}')

    elif 500<=Total<=999:
        Total_Discount = Total * 0.10
        print(f'Discount : {Total_Discount:.2f}')
        Final_price = Total-Total_Discount
        print (f'Final Amount to Pay : {Final_price:.2f}')

    else:
        print(f'Discount : {Total_Discount:.2f}')
        Final_price = Total-Total_Discount
        print(f'Final Amount to Pay : {Final_price:.2f}')

elif Member == 'n':
    if Total >= 1000:
        Total_Discount = Total * 0.05
        print(f'Discount : {Total_Discount:.2f}')
        Final_price = Total-Total_Discount
        print (f'Final Amount to Pay : {Final_price:.2f}')

    elif Total < 1000:
        print(f'Discount : {Total_Discount:.2f}')
        Final_price = Total-Total_Discount
        print(f'Final Amount to Pay : {Final_price:.2f}')