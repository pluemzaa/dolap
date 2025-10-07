motorcycleHours = 0
carHours = 0
motorcycleFee = 0
carFee = 0

while True:
    vehicle = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    hours = float(input("Please enter the number of parking hours: "))

    if vehicle not in [1, 2]:
        print("Invalid vehicle type")
        break  # ❗ จบโปรแกรมทันที

    if hours <= 0:
        print("Please enter a valid number of parking hours")
    else:
        if vehicle == 1:
            if hours < 1:
                fee = 0.00
            else:
                fee = 10 + (hours - 1) * 5
            print(f"Parking fee: {fee:.2f} THB")
            motorcycleHours += hours
            motorcycleFee += fee

        elif vehicle == 2:
            if hours < 1:
                fee = 0.00
            else:
                fee = 30 + (hours - 1) * 15
            print(f"Parking fee: {fee:.2f} THB")
            carHours += hours
            carFee += fee

    cont = input("Do you want to continue? (y/n): ").lower()
    print("------------------------------")
    if cont == 'n':
        break

# แสดงผลลัพธ์สรุป
print("VT Hours Cost")
if motorcycleHours > 0:
    print(f"1 {motorcycleHours:.2f} {motorcycleFee:.2f}")
if carHours > 0:
    print(f"2 {carHours:.2f} {carFee:.2f}")
total = motorcycleFee + carFee
print(f"Total {total:.2f} THB")