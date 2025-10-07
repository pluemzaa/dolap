mb = input('Membership (y/n) :')
p = int(input('Total amount :'))
d = 0
if mb == ('y'):
    if p >= 1000:
        d=(p/100)*20
    else:
        d=(p/100)*10
else:
    if p >= 1000:
        d=(p/100)*5

print (f'Discount :{d:.2f}')
total = p-d
print (f"Final Amount to Pay :{total:.2f}")