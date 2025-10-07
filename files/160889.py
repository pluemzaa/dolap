MotorPrice = 0
CarPrice = 0
P1 = 0
P2 = 0
time1 = 0
time2 = 0

while True:
    type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    time = float(input("Please enter the number of parking hours: "))
    if type == 1:
        if time <= 0:
            print("Please enter a valid number of parking hours")
            time = 0
        elif time < 1 and time > 0:
            P1 = 0
            MotorPrice = MotorPrice + 0
            time1 = time1 + time
        elif time == 1:
            P1 = 10
            MotorPrice = MotorPrice + 10
            time1 = time1 + time
        elif time > 1:
            P1 = (10+((time-1)*5))
            MotorPrice = MotorPrice + (10+((time-1)*5))
            time1 = time1 + time
        print(f"Parking fee: {P1:.2f} THB")

    elif type == 2:
        if time <= 0:
            print("Please enter a valid number of parking hours")
            time = 0
        elif time < 1 and time > 0:
            P2 = 0
            CarPrice = CarPrice + 0
            time2 = time2 + time
        elif time == 1:
            P2 = 30
            CarPrice = CarPrice + 30
            time2 = time2 + time
        elif time > 1:
            P2 = (30+((time-1)*15))
            CarPrice = CarPrice + (30+((time-1)*15))
            time2 = time2 + time
        print(f"Parking fee: {P2:.2f} THB")

    else:
        print("Invalid vehicle type")

    select = input("Do you want to continue? (y/n): ")
    if select == "y":
        print("------------------------------")
        continue
    else:
        break
print("------------------------------")
print("VT Hours Cost")
if time1 > 0:
    print(f"1 {time1:.2f} {MotorPrice:.2f}")
if time2 > 0:
    print(f"2 {time2:.2f} {CarPrice:.2f}")
print(f"Total {CarPrice+MotorPrice:.2f} THB")