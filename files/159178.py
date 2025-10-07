ct = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
hs = float(input("Please enter the number of parking hours: "))

if ct == 1:
    if 0< hs < 1:
        price = 0
        print(f"Parking fee {price:.2f} THB")
    elif hs >= 1:
        price = 10 + ((hs-1)*5)
        print(f"Parking fee {price:.2f} THB")
    else :
        print("Please enter a valid number of parking hours")
elif ct == 2 :
    if 0 < hs < 1:
        price = 0
        print(f"Parking fee {price:.2f} THB")
    elif hs >= 1:
        price = 30 + ((hs-1)*15)
        print(f"Parking fee {price:.2f} THB")
    else :
        print("Please enter a valid number of parking hours")  
else:
     print("Invalid vehicle type")