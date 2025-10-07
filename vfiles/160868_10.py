motorcycleCount = 0
carCount = 0
motorcycleHours = 0
carHours = 0
motorcycleFee = 0
carFee = 0


while True:
    vehicle = int(input("Please enter vehicle type (1:Motorcycle, 2:Personal Car): "))

    if vehicle == 1:
        hours = float(input("Please enter the number of parking hours: "))
        if hours <= 0:
            print("Please enter a valid number of parking hours")
        else:
            if hours > 0 and hours < 1:
                print(f"Parking fee: 0.00 THB")
            else:
                if hours >= 1:
                    fee = 10 + (hours - 1) * 5
            print(f"Parking fee: {fee:.2f} THB")
            motorcycleCount += 1
            motorcycleFee += fee
            motorcycleHours += hours

    elif vehicle == 2:
        hours = float(input("Please enter the number of parking hours: "))
        if hours <= 0:
            print("Please enter a valid number of parking hours")
        else:
            if hours > 0 and hours < 1:
                print(f"Parking fee: 0.00 THB")
            else:
                if hours >= 1:
                    fee = 30 + (hours - 1) * 15
            print(f"Parking fee: {fee:.2f} THB")
            carCount += 1
            carFee += fee
            carHours += hours

    else:
        print("Invalid menu")

    con = input("Do you want to continue? (y/n): ")
    if con == 'n':
        break
print("VT Hours Cost")
if motorcycleCount > 0:
    print("1" f" {motorcycleHours:.2f} {motorcycleFee:.2f}")
if carCount > 0:
    print("2" f" {carHours:.2f} {carFee:.2f}")

totalFee = motorcycleFee + carFee
print("Total" f" {totalFee:.2f} THB")