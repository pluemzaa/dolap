_type = float(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
hours = float(input("Please enter the number of parking hours: "))

if hours >= 0:
    if hours < 1:
        print("Parking fee: 0.00 THB")
    else :
        if _type == 1: # Motorcycle
            fee = 10 if hours <= 1 else 10+((hours-1) * 5)
            print(f"Parking fee: {fee:.2f} THB")
        elif _type == 2: # Personal Car
            fee = 30 if hours <= 1 else 30+((hours-1) * 15)
            print(f"Parking fee: {fee:.2f} THB")
        else : # Invalid
            print("Invalid vehicle type")
else :
    print("Please enter a valid number of parking hours")