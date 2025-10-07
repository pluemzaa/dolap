type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
time = float(input("Please enter the number of parking hours: "))
total = float(0)

if type == 1 :
    if time <= 0:
        print ("Please enter a valid number of parking hours")
    elif time < 1 :
        print ("Parking fee: %.2f THB" %total)
    elif time >= 1:
        total = total+ (10+((time-1)*5))
        print ("Parking fee: %.2f THB" %total)
elif  type == 2 :
    if time <= 0:
        print ("Please enter a valid number of parking hours")
    elif time < 1 :
        print ("Parking fee: %.2f THB" %total)
    elif time >= 1:
        total = total+ (30+((time-1)*15))
        print ("Parking fee: %.2f THB" %total)
else :
    print ("Invalid vehicle type")