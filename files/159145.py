car = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
time = float(input("Please enter the number of parking hours: "))
if car == 1 or car ==2:
    if time>0: 
        if time <1:
            price = 0
        elif car ==1:
            price = ((time-1)*5)+10
        elif car ==2:
            price = ((time-1)*15)+30
        print(f"Parking fee: {price:.2f} THB")

    else:
        print("Please enter a valid number of parking hours")
    
    
else:
    print("Invalid vehicle type")