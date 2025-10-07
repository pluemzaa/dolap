feem = 0
hm = 0
hc = 0
feec = 0
while True:
    v = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    h = float(input("Please enter the number of parking hours: "))
    if v == 1:
        if 0< h < 1:
            hc+=h
            print("Parking fee: 0.00 THB")
        elif h>= 1:
            feem += 10+ (h-1)*5
            hm += h
            print(f"Parking fee: {feem:.2f} THB")
        else:
            print("Please enter a valid number of parking hours")
    elif v == 2:
        if 0 < h < 1:
            hc+=h
            print("Parking fee: 0.00 THB")
        elif h>= 1:
            feec += 30 + (h - 1)*15
            hc += h
            print(f"Parking fee: {feec:.2f} THB")
        else: 
            print("Please enter a valid number of parking hours")
    else:
        print("Invalid vehicle type")
    
    c = input("Do you want to continue? (y/n): ")
    print("------------------------------")
    if c == "n":
        break

print("VT Hours Cost")
print(f"1 {hm:.2f} {feem:.2f}")
print(f"2 {hc:.2f} {feec:.2f}")
f = feem + feec
print(f"Total {f:.2f} THB")