type1 = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
hours = float(input("Please enter the number of parking hours: "))
if type1 == "1" or type1 == "2":
    if hours > 0:
        if hours < 1:
           res = 0
        elif type1 == "1":
            res = 5*(hours-1)+10
        elif type1 == "2":
            res = 15*(hours-1)+30
        print(f"Parking fee: {res:.2f} THB")
    else:
        print("Please enter a valid number of parking hours")    
else:
    print("Invalid vehicle type")