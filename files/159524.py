type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
hours = float(input("Please enter the number of parking hours: "))


if type == 1 :
    if hours == 1 :
        price = 10
        print(f"Parking fee: {price:.2f} THB ") 
    elif hours > 1 :
        price = 10 + ((hours-1)*5)
        print(f"Parking fee: {price:.2f} THB ") 
    elif hours >= 0 < 1 :
        price = 0
        print(f"Parking fee: {price:.2f} THB ") 
    else:
        print ("Please enter a valid number of parking hours" )
elif type == 2 :
    if hours == 1 :
        price = 30
        print(f"Parking fee: {price:.2f} THB ") 
    elif hours > 1 :
        price = 30 + ((hours-1)*15)
        print(f"Parking fee: {price:.2f} THB ") 
    elif hours >= 0 < 1 :
        price = 0
        print(f"Parking fee: {price:.2f} THB ") 
    else:
        print ("Please enter a valid number of parking hours")
else :
    print ("Invalid vehicle type")