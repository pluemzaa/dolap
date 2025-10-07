E = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car):"))
O = float(input("Please enter the number of parking hours:"))
r=0
if O >0:
    if E <= 2 and E > 0 :
        if O >= 1:
            if E==1:
                if O==1:
                    r=r+10
                    print(f"Parking fee:{r:.2f} THB")
                elif O >1:
                    r=((O-1)*5)+10
                    print(f"Parking fee:{r:.2f} THB")
            else:
                if O==1:
                    r=r+30
                    print(f"Parking fee:{r:.2f} THB")
                elif O >1:
                    r=((O-1)*15)+30
                    print(f"Parking fee:{r:.2f} THB")
        else:
            print(f"Parking fee:{r:.2f} THB")
    else:
        print("Invalid vehicle type")
else:
    print("Please enter a valid number of parking hours")