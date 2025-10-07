car = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
hours = float(input("Please enter the number of parking hours: "))
if car == 1 or car == 2 :
    if hours <= 0 :
            print("Please enter a valid number of parking hours")
    else :        
        if car == 1:
            if hours < 1 and hours > 0 :
                print(f"Parking fee: 0.00 THB")
            else :
                print(f"Parking fee: {((hours-1)*5)+10:.2f} THB")
        else :
            if hours < 1 and hours > 0 :
                print(f"Parking fee: 0.00 THB")
            else :
                print(f"Parking fee: {((hours-1)*15)+30:.2f} THB")

else :
    print("Invalid vehicle type")