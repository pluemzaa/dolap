sum_time1 = 0.0
fee1 = 0.0
sum_time2 = 0.0
fee2 = 0.0

while True:
    try:
        type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    except ValueError:
        print("Invalid vehicle type")
        break

    if type not in [1, 2]:
        print("Invalid vehicle type")
        break

    try:
        park_time = float(input("Please enter the number of parking hours: "))
    except ValueError:
        print("Please enter a valid number of parking hours")
        break

    if park_time <= 0:
        print("Please enter a valid number of parking hours")
        break

    if park_time < 1:
        fee = 0
    elif park_time == 1:
        fee = 10 if type == 1 else 30
    else:
        fee = 10 + (park_time - 1) * 5 if type == 1 else 30 + (park_time - 1) * 15

    print(f"Parking fee: {fee:05.2f} THB")
    ans = input("Do you want to continue? (y/n): ")
    print("------------------------------")

    if type == 1:
        sum_time1 += park_time
        fee1 += fee
    elif type == 2:
        sum_time2 += park_time
        fee2 += fee

    if ans.lower() == "n":
        break

print("VT Hours Cost")
if sum_time1 > 0:
    print(f"1 {sum_time1:.2f} {fee1:05.2f}")
if sum_time2 > 0:
    print(f"2 {sum_time2:.2f} {fee2:05.2f}")
print("Total", "{:.2f}".format(fee1 + fee2), "THB")