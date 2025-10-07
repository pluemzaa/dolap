motorcycleCount = 0
carCount = 0
motorcycleHours = 0
carHours = 0
motorcycleFee = 0
carFee = 0


while True:
    vehicle = int(input("Enter menu (1=Motorcycle, 2=Personal Car): "))

    if vehicle == 1:
        print("You select Motorcycle")
        hours = float(input("Please enter number of parking hours: "))
        if hours <= 0:
            print("Please enter a valid number of parking hours")
        else:
            if hours < 1:
                fee = 0
            else:
                fee = 10 + (hours - 1) * 5
            print(f"Parking fee: {fee:.2f} THB")
            motorcycleCount += 1
            motorcycleFee += fee
            motorcycleHours += hours

    elif vehicle == 2:
        print("You select Personal Car")
        hours = float(input("Please enter number of parking hours: "))
        if hours <= 0:
            print("Please enter a valid number of parking hours")
        else:
            if hours < 1:
                fee = 0
            else:
                fee = 30 + (hours - 1) * 15
            print(f"Parking fee: {fee:.2f} THB")
            carCount += 1
            carFee += fee
            carHours += hours

    else:
        print("Invalid menu")

    con = input("Continue? (y/n): ")
    if con == 'n':
        break
print("VT Hours Cost")
if motorcycleCount > 0:
    print(f"1 {motorcycleHours:.2f} {motorcycleFee:.2f}")
if carCount > 0:
    print(f"2 {carHours:.2f} {carFee:.2f}")

totalFee = motorcycleFee + carFee
print(f"Total {totalFee:.2f} THB")