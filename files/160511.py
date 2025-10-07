b1 = 0
b2 = 0
d1 = 0
d2 = 0
while True:
    a = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
    b = float(input("Please enter the number of parking hours: "))
    if a == "1" or a == "2":
        if b > 0:
            if a == "1":
                if b >= 1:
                    c = 10 + ((b-1)*5)
                    b1 = b1 + b
                    d1 = d1 + c
                else:
                    c = 0
                    b1 = b1 + b
            else:
                if b >= 1:
                    c = 30 + ((b-1)*15)
                    b2 = b2 + b
                    d2 = d2 + c
                else:
                    c = 0
                    b2 = b2 + b
            print(f"Parking fee: {c:.2f} THB")
        else:
            print("Please enter a valid number of parking hours")

    else:
        print("Invalid vehicle type")
    
    z = input("Do you want to continue? (y/n): ")
    print("------------------------------")
    if z == "y":
        continue
    else:
        break

d = d1 + d2
print("VT Hours Cost")
if b1 > 0 and b2 > 0:
    print(f"1 {b1:.2f} {d1:.2f}")
    print(f"2 {b2:.2f} {d2:.2f}")
elif b1 > 0:
    print(f"1 {b1:.2f} {d1:.2f}")
else:
    print(f"2 {b2:.2f} {d2:.2f}")
print(f"Total {d:.2f} THB")