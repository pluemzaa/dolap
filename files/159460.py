verhicle = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
duration = float(input("Please enter the number of parking hours: "))

if verhicle == 1:
        if duration > 0:
            if duration == 1:
                cal = duration * 10
                print(f"Parking fee: {cal:.2f} THB")
            elif duration < 1:
                cal1 = duration * 0
                print(f"Parking fee: {cal1:.2f} THB")
            elif duration > 1:
                cal2 = duration * 5 + 5
                print(f"Parking fee: {cal2:.2f} THB")
        else:
                print("Please enter a valid number of parking hours")
elif verhicle == 2:
        if duration > 0:
            if duration == 1:
                cal = duration * 30
                print(f"Parking fee: {cal:.2f} THB")
            elif duration < 1:
                cal1 = duration * 0
                print(f"Parking fee: {cal1:.2f} THB")
            elif duration > 1:
                cal2 = duration * 15 + 15
                print(f"Parking fee: {cal2:.2f} THB")
        else:
                print("Please enter a valid number of parking hours")
else:
    print("Invalid vehicle type")