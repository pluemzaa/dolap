x = str(input('Membership (y/n) : '))
z = int(input('Total amount : '))
d= 0
if x == 'y' :
    if z >= 1000 :
        d = z*0.20
    elif z >= 500 <=999 :  
        d = z*0.10  
else :
    if z >= 1000:
        d = z*0.05
final = z - d 
print(f'Discount : {d:.2f}')  
print(f'Final Amount to Pay : {final:.2f}')