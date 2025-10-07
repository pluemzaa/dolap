while True:
    x = input('Membership (y/n) :')
    if x == 'y':
        y = int(input('Total amount : '))
        if y >= 1000:
            d = (20/100)*y
            print("Discount :",d)
            print('Final Amount to Pay :',y-d)
            break
    if y < 1000 and y >= 500:
        y = int(input('Total amount : '))
        d =(10/100)*y
        print("Discount :",d)
        print('Final Amount to Pay :',y-d)
        break
    if x == 'n':
        y = int(input('Total amount : '))
        if y >= 1000:
            d = (5/100)*y
            print("Discount :",d)
            print('Final Amount to Pay :',y-d)
            break
    elif y < 500:
        d = 0.00
        print("Discount :",d)
        print('Final Amount to Pay :',y-d)