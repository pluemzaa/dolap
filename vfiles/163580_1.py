x = str(input('Membership (y/n) : '))
z = int(input('Total amount : '))

if x == 'y' :
    if z > 1000 :
        d = (z*20)/100
    elif z >= 500 <=999 :  
        d = (z*10)/100 
        print(f'Discount : {d:.2f}')  
        print(f'Final Amount to Pay : {z-d:.2f}') 
        
        
else :
    print('Discount : ',(z*5)/100)
    r= (z-((z*5)/100) )
    print (f'Final Amount to Pay : {r:.2f}' )