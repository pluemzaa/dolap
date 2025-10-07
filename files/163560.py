m=input('Membership (y/n) : ')
t=float(input('Total amount : '))
d=0
if m=='y':
    if t>=1000:
        d=t*0.20
    elif t>=500:
        d=t*0.10
else:
    if t>=1000:
        d=t*0.05
total=t-d
print('Discount : ',f'{d:.2f}')
print('Final Amount to Pay : ',f'{total:.2f}')