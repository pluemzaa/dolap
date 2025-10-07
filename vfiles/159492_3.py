vehicle_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))


if vehicle_type != 1 and vehicle_type != 2:
    print("Invalid vehicle type")
else:
  
    parking_hours = float(input("Please enter the number of parking hours: "))

 
    if parking_hours <= 0:
        print("Please enter a valid number of parking hours")
    else:
       
        if parking_hours < 1:
            fee = 0.00
        else:
          
            if vehicle_type == 1:
                fee = 10 + (parking_hours - 1) * 5
          
            elif vehicle_type == 2:
                fee = 30 + (parking_hours - 1) * 15

    
        print(f"Parking fee: {fee:.2f} THB")