m = input('Membership (y/n) : ')
t = int(input('Total amount : '))
d = 0
if m == "y":
    if t >= 1000:
        d = t*0.20
    if t >= 500 and t <= 999:
        d = t*0.10
else:
    if t >= 1000:
        d = t*0.05
a = t-d
print(f'Discount : {d:.2f}')
print(f'Final Amount to Pay : {a:.2f}')