mb=input('Membership (y/n) :')
ta=float(input('Total amount :'))

if 500<=ta:
    if 500<=ta<=999:
        if mb=='y':
            ds=ta*0.1
        else:
            ds=0.0
    elif ta>=1000:
        if mb =='y':
            ds=ta*0.2
        else:
            ds=ta*0.05
else:
    ds=0.00

fa=ta-ds

print(f'Discount :{ds:.2f}')
print(f'Final Amount to Pay :{fa:.2f}')