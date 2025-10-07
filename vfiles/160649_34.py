park_time1 = 0.0
sum_time1 = 0.0
fee1 = 0.0

park_time2 = 0.0
sum_time2 = 0.0
fee2 = 0.0

ans = ""

type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))

if type == 1:
    park_time1 = float(input("Please enter the number of parking hours: "))
    if park_time1 < 0:
        print("Please enter a valid number of parking hours")
    elif park_time1 < 1:
        fee1 += 0
        sum_time1 += park_time1
    elif park_time1 == 1:
        fee1 += 10
        sum_time1 += park_time1
    else:
        fee1 += (park_time1 * 5) + 5
        sum_time1 += park_time1

    print(f"Parking fee: {fee1:.2f} THB")
    ans = input("Do you want to continue? (y/n): ")
    print("------------------------------")

elif type == 2:
    park_time2 = float(input("Please enter the number of parking hours: "))
    if park_time2 < 0:
        print("Please enter a valid number of parking hours")
    elif park_time2 < 1:
        fee2 += 0
        sum_time2 += park_time2
    elif park_time2 == 1:
        fee2 += 30
        sum_time2 += park_time2
    else:
        fee2 += (park_time2 * 15) + 15
        sum_time2 += park_time2

    print(f"Parking fee: {fee2:.2f} THB")
    ans = input("Do you want to continue? (y/n): ")
    print("------------------------------")

else:
    print("Invalid vehicle type")

while ans == "y":
    type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    if type == 1:
        park_time1 = float(input("Please enter the number of parking hours: "))
        if park_time1 <= 0:
            print("Please enter a valid number of parking hours")
            ans = input("Do you want to continue? (y/n): ")
            break
        elif park_time1 < 1:
            fee1 += 0
        elif park_time1 == 1:
            fee1 += 10
        else:
            fee1 += (park_time1 * 5) + 5
        sum_time1 += park_time1
        print(f"Parking fee: {fee1:.2f} THB")
        ans = input("Do you want to continue? (y/n): ")
        print("------------------------------")

    elif type == 2:
        park_time2 = float(input("Please enter the number of parking hours: "))
        if park_time2 <= 0:
            print("Please enter a valid number of parking hours")
            ans = input("Do you want to continue? (y/n): ")
            break
        elif park_time2 < 1:
            fee2 += 0
        elif park_time2 == 1:
            fee2 += 30
        else:
            fee2 += (park_time2 * 15) + 15
        sum_time2 += park_time2
        print(f"Parking fee: {fee2:.2f} THB")
        ans = input("Do you want to continue? (y/n): ")
        print("------------------------------")

    else:
        print("Invalid vehicle type")
        break

if ans == "n":
    print("VT Hours Cost")
    if sum_time1 > 0.0:
        print(f"1 {sum_time1:.2f} {fee1:.2f}")
    if sum_time2 > 0.0:
        print(f"2 {sum_time2:.2f} {fee2:.2f}")
    print("Total {:.2f} THB".format(fee1 + fee2))