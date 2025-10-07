cost1 = 0
cost2 = 0

time1 = 0
time2 = 0

while True:
    t = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
    dt = float(input("Please enter the number of parking hours: "))

    fh = 10
    nh = 5
    
    if t == "2":
        fh = 30
        nh = 15

    if dt < 1:
        fh = 0
        nh = 0
        
    if (t == "1" or t == "2") and dt > 0:
        fee = (dt - 1) * nh + (1 * fh)

        print(f"Parking fee: {fee:.2f} THB")
        
        if t == "1":
            cost1 += fee
            time1 += dt
        else:
            cost2 += fee
            time2 += dt
            
    elif not (t == "1" or t == "2"):
        print("Invalid vehicle type")
        
    elif not dt > 0:
        print("Please enter a valid number of parking hours")
    
    con = input("Do you want to continue? (y/n): ")
    
    print("------------------------------")
    
    if con == "n":
        break

print("VT Hours Cost")

if time1 > 0 or cost1 > 0:
    print(f"1 {time1:.2f} {cost1:.2f}")
    
if time2 > 0 or cost2 > 0:
    print(f"2 {time2:.2f} {cost2:.2f}")
    
print(f"Total {(cost1 + cost2):.2f} THB")