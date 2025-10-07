M = str(input('Membership (y/n) :'))
Amo = float(input('Total amount :'))
if M == 'y' :
    if 500<=Amo<=999:
        Discount = (Amo)*0.1
        print(f'Discount :{Discount:.2f}')
        final_amo = Amo - Discount
        print(f'Final Amount to Pay : {final_amo:.2f}')
    elif Amo>=1000:
        Discount = (Amo)*0.2
        print(f'Discount :{Discount:.2f}')
        final_amo = Amo - Discount
        print(f'Final Amount to Pay : {final_amo:.2f}')
    else:
        Discount = 0
        print(f'Discount :{Discount:.2f}')
        final_amo = Amo - Discount
        print(f'Final Amount to Pay : {final_amo:.2f}')
elif M == 'n' :
    if Amo>=1000:
        Discount = (Amo)*0.05
        print(f'Discount :{Discount:.2f}')
        final_amo = Amo - Discount
        print(f'Final Amount to Pay : {final_amo:.2f}')
    else:
        Discount = 0
        print(f'Discount :{Discount:.2f}')
        final_amo = Amo - Discount
        print(f'Final Amount to Pay : {final_amo:.2f}')