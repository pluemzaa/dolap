typec = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
time = float(input("Please enter the number of parking hours: "))
if typec == 1 or typec == 2:
    if time > 0 :
        if typec == 1 :
            pf1 = 10
            if time < 1 :
                print("Parking fee: 0.00 THB")
            elif time == 1:
                print(f"Parking fee: {pf1:.2f} THB")
            elif time > 1:
                time = time - 1
                pf = 10 + (time*5)
                print(f"Parking fee: {pf:.2f} THB")    

        elif typec == 2 :
            pf1 = 30
            if time < 1 :
                print("Parking fee: 0.00 THB")
            elif time == 1 :
                print(f"Parking fee: {pf1:.2f} THB")
            elif time >= 1 :
                time = time - 1
                pf = 30 + (time*15)
                print(f"Parking fee: {pf:.2f} THB")
    elif time <= 0 :
        print("Please enter a valid number of parking hours")
else :
    print("Invalid vehicle type")