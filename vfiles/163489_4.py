mem = input('Membership (y/n) : ')
Toamount = int(input('Total amount : '))

discount = 0
if mem == "y":
    if Toamount >= 1000:
        discount = Toamount*0.2
    elif Toamount >=500:
        discount =  Toamount*0.1
else:
     Toamount >= 1000
     discount = Toamount*0.05

print('Discount : %.2f'% discount)
print('Final Amount to Pay : %.2f' %(Toamount - discount))