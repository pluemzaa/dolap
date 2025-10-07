car = 0.00
hcar = 0.00
mon = 0.00
hmon = 0.00
while True :
    v = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    h = float(input("Please enter the number of parking hours: "))
    if v not in [1,2]  :
        print ("Invalid vehicle type")
    if h <= 0 :
        print("Please enter a valid number of parking hours")
    else :
        if v == 1 and h < 1  :     
            print("Parking fee: 0.00 THB")
            hmon += h
        elif v == 2 and h < 1  :     
            print("Parking fee: 0.00 THB")
            hcar += h
        elif v == 1 :
                c = 5
                p = 10 + ((h-1)*c)
                print(f"Parking fee: {p:.2f} THB")
                mon += p
                hmon += h
        elif v == 2  :
                c = 15
                p = 30 + ((h-1)*c)
                print(f"Parking fee: {p:.2f} THB")
                car += p
                hcar += h
    c  = input ("Do you want to continue? (y/n): ")
    if c == "y" :
        print ("------------------------------")
    elif c == "n" : 
        break
print ("------------------------------")
print("VT Hours Cost")
if hmon > 0:
    print(f"1 {hmon:.2f} {mon:.2f}")
if hcar > 0:
    print(f"2 {hcar:.2f} {car:.2f}")
print (f"Total {car+mon:.2f} THB")