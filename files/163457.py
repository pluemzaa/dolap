m = input('Membership (y/n) : ')
t = int(input("Total amount : "))
if m == 'y' :
    if t >= 1000 :
        d = t*0.2
        print(f'Discount : {d:.2f}')
    elif t >= 500 :
        d = t*0.1
        print(f'Discount : {d:.2f}')
    elif t >= 999:
        d = t*0.1
        print(f'Discount : {d:.2f}')
    else :
        d = 0
        print("Discount : 0.00") 
elif m == 'n':
    if t >= 1000 :
        d = t*0.05
        print(f'Discount : {d:.2f}')
    else :
        d = 0
        print("Discount : 0.00")    
all = t-d
print(f'Final Amount to Pay : {all:.2f}')