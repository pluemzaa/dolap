motorcycleCount = 0
carCount = 0
motorcycleHours = 0
carHours = 0
motorcycleFee = 0
carFee = 0

while True:
    vehicle = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    hours = float(input("Please enter the number of parking hours:"))
    if vehicle == 1:
        if hours <= 0:
            print("Please enter a valid number of parking hours")
        else:
            if hours < 1:
                fee = 0.00
            else:

                fee = 10 + (hours-1) * 5
            print(f"Parking fee: {fee:.2f} THB" )
            motorcycleCount += 1
            motorcycleFee += fee
            motorcycleHours += hours

    elif vehicle == 2:
        if hours <= 0:
            print("Please enter a valid number of parking hours")
        else:
            if hours < 1:
                fee = 0.00
            else:

                fee = 30 + (hours-1) * 15
            print(f"Parking fee: {fee:.2f} THB" )
            carCount += 1
            carFee += fee
            carHours += hours
    else:
        print("Invalid vehicle type")
        
    con = input("Do you want to continue? (y/n): ")
    print("------------------------------")
    if con == "n":
        break
print("VT Hours Cost")
if motorcycleCount > 0:
    print("1" f"{motorcycleHours:.2f}{motorcycleFee:.2f}")
if carCount > 0:
    print("2" f"{carHours:.2f}{carFee:.2f}")
    
totalFee = motorcycleFee + carFee
print("Total" f"{totalFee:.2f} THB")