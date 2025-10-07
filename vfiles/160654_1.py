x = 1
while x == 1 :
    typec = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    hour = float(input("Please enter the number of parking hours: "))
    if typec !=1 and typec != 2 :
            print("Invalid vehicle type")
    elif hour <= 0:
        print("Please enter a valid number of parking hours")
        
    percp = 30
    permt = 10
    if typec == 2 :
        if hour >0 and hour <1 :
            percp = 0
            print(f"Parking fee: {percp:.2f} THB")
        elif hour >= 1 :
            percp = percp + (15 * (hour - 1))
            print(f"Parking fee: {percp:.2f} THB")
    elif typec == 1 :
        if hour >0 and hour <1 :
            permt = 0
            print("Parking fee: 0.00 THB")
        elif hour >= 1 :
            permt = permt + (5 * (hour - 1))
            print(f"Parking fee: {permt:.2f} THB")

    x = x - 1
    boo = input("Do you want to continue? (y/n): ").lower()
    print("------------------------------")
    if boo == "y":
        x = x + 1

x = [permt,percp]
if permt or percp :
    print("VT Hours Cost")
    print(f"1 {hour:.2f} {permt:.2f}")
    print(f"2 {hour:.2f} {percp:.2f}")