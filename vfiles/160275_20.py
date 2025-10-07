total_cost = 0 
recvfds = []
con = None
while True:
    vec = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car):")
    hours = float(input("Please enter the number of parking hours: "))
    if vec == '1' or vec == '2':
        if hours > 0:
            if hours < 1:
                res = 0
            elif vec == '1':
                res = 5*(hours-1)+10
            elif vec == '2':
                res = 15*(hours-1)+30
            print(f"Parking fee: {res:.2f} THB")
            con = input("Do you want to continue? (y/n):")
            recvfds.append((vec, hours, res))
            total_cost += res
            print("------------------------------")
        if con == 'y':
            continue
        elif con == 'n':
            print("VT Hours Cost")
            for v, h, c in recvfds:
                print(f"{v} {h:.2f} {c:.2f}")
            print(f"Total {total_cost:.2f} THB")
            break
        else:
            print("Please enter a valid number of parking hours")
            break
    else:
        print("Invalid vehicle type")
        break