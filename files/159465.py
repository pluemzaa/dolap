v = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
hour = float(input("Please enter the number of parking hours: "))
car = 30
mor = 10
if v == 1 :
    if hour >= 0:
        if hour < 1:
            price = mor*0
        elif hour >= 1 and hour < 2:
            price = mor
        else:
            price = mor+((hour-1)*5)
        print(f"Parking fee: {price:.2f} THB")
    else:
        print("Please enter a valid number of parking hours")
elif v == 2 :
    if hour >= 0:
        if hour < 1:
            price = car*0
        elif hour >= 1 and hour < 2:
            price = car
        else:
            price = car+((hour-1)*15)
        print(f"Parking fee: {price:.2f} THB")
    else:
        print("Please enter a valid number of parking hours")
else :
    print ("Invalid vehicle type")