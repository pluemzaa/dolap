c = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
h = float(input("Please enter the number of parking hours:"))
if c ==1:
    if h > 0:
        if h ==1:
            price = 10 * h
            print(f"Parking fee: {price:.2f} THB")
        elif h >1:
            price = 5 * (h-1) + 10
            print(f"Parking fee: {price:.2f} THB")
        else :
            price = 0 * h
            print(f"Parking fee: {price:.2f} THB")
    else:
         print("Please enter a valid number of parking hours")
elif c ==2:
    if h > 0 :
         if h ==1:
             price = 30 * h
             print(f"Parking fee: {price:.2f} THB")
         elif h >1:
             price = 15 * (h-1) + 30
             print(f"Parking fee: {price:.2f} THB")
         else :
             price = 0 * h
             print(f"Parking fee: {price:.2f} THB")
    else:
         print("Please enter a valid number of parking hours")
else:
     print("Invalid vehicle type")