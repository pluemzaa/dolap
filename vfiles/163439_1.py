member = True if input('Membership (y/n) : ') == 'y' else False
amount = int(input('Total amount : '))

dis = 0
if member:
    if amount >= 1000:
        dis = amount*0.2
    elif amount >= 500:
        dis = amount*0.1
elif amount >= 1000:
    dis = amount*0.05
        
print('Discount : %.2f' %dis)
print('Final Amount to Pay : %.2f' %(amount - dis))