x = 1
vt_costs = []
total_cost = 0


while x == 1 :
    typec = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    hour = float(input("Please enter the number of parking hours: "))
    if typec !=1 and typec != 2 :
            print("Invalid vehicle type")
    elif hour <= 0:
        print("Please enter a valid number of parking hours")
        
    
    if typec == 2 :
        cost = 30
        if hour >0 and hour <1 :
            cost = 0
            print(f"Parking fee: {cost:.2f} THB")
        elif hour >= 1 :
            cost = cost + (15 * (hour - 1))
            print(f"Parking fee: {cost:.2f} THB")
    elif typec == 1 :
        cost = 10
        if hour >0 and hour <1 :
            cost = 0
            print("Parking fee: 0.00 THB")
        elif hour >= 1 :
            cost = cost + (5 * (hour - 1))
            print(f"Parking fee: {cost:.2f} THB")
    vt_costs.append((typec, hour,cost))
    total_cost += cost

    x = x - 1
    boo = input("Do you want to continue? (y/n): ").lower()
    print("------------------------------")
    if boo == "y":
        x = x + 1

print("VT Hours Cost")

for i in vt_costs:
    print(f"{int(i[0])} {i[1]:.2f} {i[2]:.2f}")
print(f"Total {total_cost:.2f} THB")