mC = 0
mH = 0
cH = 0
cC = 0
while True :
    car = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    h = float(input("Please enter the number of parking hours: "))
    if 0 < h :
        if car == 1 :
            mH += h
            if h < 1 :
                print("Parking fee: 0.00 THB")    
            elif h > 1 :
                m2 = ((h-1)*5)+10
                mC += m2
                print(f'Parking fee:{m2: .2f} THB')   
            elif h == 1 :
                m1 = h*10
                mC += m1
                print(f'Parking fee:{m1: .2f} THB') 
        elif car == 2 :
            cH += h
            if h < 1 :
                print("Parking fee: 0.00 THB")    
            elif h == 1 :
                c1 = (h*30)
                cC += c1 
                print(f'Parking fee:{c1: .2f} THB')
            elif h > 1 :
                c2 = (((h-1)*15)+30)
                cC += c2             
                print(f'Parking fee:{c2: .2f} THB')
        else :
            print("Invalid vehicle type")           
    else :   
        print("Please enter a valid number of parking hours ")
          
        
    con = input("Do you want to continue? (y/n): ")         
    print('------------------------------ ')
    if con == 'n' :
        break
if mH or cH >0 :
    print("VT Hours Cost") 
    if mH > 0:
        print(f'1 {mH: .2f} {mC: .2f}')
if cH > 0 :
    print(f'2 {cH: .2f} {cC: .2f}')
al = mC+cC
print(f'Total {al: .2f} THB')