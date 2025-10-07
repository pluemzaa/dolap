carprice = 0
carcount = 0
motoprice = 0
motocount = 0
total = 0

while True:
    vc = float(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car):"))
    if vc == 1:
        motocount = float(input("Please enter the number of parking hours:"))
        if motocount <= 0:
            print("Please enter a valid number of parking hours")
        elif motocount > 0 and motocount < 1:
            print("Parking fee: 0.00 THB")
        elif motocount >=1:
            motoprice = 10 + (motocount - 1) * 5 
            print(f"Parking fee:{motoprice:.2f} THB")
    elif vc == 2:
        carcount = float(input("Please enter the number of parking hours:"))
        if carcount <= 0:
            print("Please enter a valid number of parking hours")
        elif carcount > 0 and carcount < 1:
            print("Parking fee: 0.00 THB")
        elif carcount >=1:
            carpricee = 30 + (carcount - 1) * 15 
            print(f"Parking fee:{carprice:.2f} THB")
    else:
        print("Invalid vehicle type")
    
    con = input("Do you want to continue? (y/n):")
    if con=='n':
        print("------------------------------")
        break
    else:
        print("------------------------------")
    print("VT Hours Cost")
    print("1", motocount, motoprice)
    print("2", carcount, carprice )
    
    total = motoprice + carprice
    print("Total "total" THB")