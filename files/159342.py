V = float(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
H = float(input("Please enter the number of parking hours: "))
cost = 0

if V<3 and V>0 and H>0:
    if V == 1:
        if H>=1:
            cost = cost+10
            H-=1
            cost+=(5*H)

    if V == 2:
        if H>=1:
            cost = cost+30
            H-=1
            cost+=(15*H)
    print(f"Parking fee: {cost:.2f} THB")

elif V>2 or V<1:
    print("Invalid vehicle type")
elif H<=0:
    print("Please enter a valid number of parking hours")