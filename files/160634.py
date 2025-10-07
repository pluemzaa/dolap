total_cost = 0
cost1 = 0
hours1 = 0
cost2 = 0
hours2 = 0
while True:
    vehicle_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    hours_input = float(input("Please enter the number of parking hours: "))
    
    if hours_input <= 0:
        print("Please enter a valid number of parking hours")
        cont = input("Do you want to continue? (y/n): ")
        print("------------------------------ ")
        if cont == "n":
             break
        else:
             continue

    if vehicle_type == 1:
        if hours_input < 1:
            cost = 0
        else:
            cost = ((hours_input - 1) * 5) + 10
        hours1 = hours1 + hours_input
        cost1 = cost1 + cost
    elif vehicle_type == 2:
        if hours_input < 1:
            cost = 0
        else:
            cost = ((hours_input - 1) * 15) + 30
        hours2 = hours2 + hours_input
        cost2 = cost2 + cost
    else:
        print("Invalid vehicle type")
        cont = input("Do you want to continue? (y/n): ")
        print("------------------------------ ")
        if cont == "n":
             break
        else:
             continue

    print("Parking fee: %.2f THB" % cost)
    total_cost = total_cost + cost
    cont = input("Do you want to continue? (y/n): ")
    print("------------------------------ ")
    if cont == "n":
        break

print("VT Hours Cost")
if hours1 > 0:
     print(f"1 {hours1:.2f} {cost1:.2f}")
if hours2 > 0:
     print(f"2 {hours2:.2f} {cost2:.2f}")
print("Total %.2f THB" % total_cost)