V = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
H = float(input("Please enter the number of parking hours: "))
F = float

if H > 0 :
    if V==1:
        if H == 1:
            F = 10
        elif H < 1:
            F = 0
        else :
            F = 10 + (H-1)*5
        print ("Parking fee: %.2f THB" %F)
    elif V==2:
        if H == 1:
            F = 30
        elif H < 1:
            F = 0
        else :
            F = 30 + (H-1)*15
        print ("Parking fee: %.2f THB" %F)
    else :
        print ("Invalid vehicle type")
else :
    print ("Please enter a valid number of parking hours")