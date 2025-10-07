v = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
h = float(input("Please enter the number of parking hours: "))
if v == 1 or v == 2:
    if v == 1:
        if h > 0:
            pay = 10+(5*(h-1)) 
        elif h==0 or h<0:  
            print("Please enter a valid number of parking hours")  
    elif v == 2:
        if h > 0:
            pay = 30+(15*(h-1))
        elif h==0 or h<0:
            print("Please enter a valid number of parking hours")
    print(f"Parking fee: {pay:.2f} THB")
else:
    print("Invalid vehicle type")