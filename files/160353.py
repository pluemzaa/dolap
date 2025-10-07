v1_h = 0
v2_h = 0
v1_p = 0
v2_p = 0
record = []

while True:
    v = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
    h = float(input("Please enter the number of parking hours: "))
    
    if v not in ["1","2"]:
        print("Invalid vehicle type")
        pass
    elif h <= 0:
        print("Please enter a valid number of parking hours")
        pass
    elif v == "1":
        v1_h += h
        if h < 1:
            fee = 0
        elif h >= 1:
            fee = 10 + ((h-1)*5)
        v1_p += fee
        print(f"Parking fee: {fee:.2f} THB")
    elif v == "2":
        v2_h += h
        if h < 1:
            fee = 0
        elif h >= 1:
            fee = 30 + ((h-1)*15)
        v2_p += fee
        print(f"Parking fee: {fee:.2f} THB")
    c = input("Do you want to continue? (y/n): ")
    print("------------------------------")
    if c == 'y':
        continue
    elif c =='n':
        break

print("VT Hours Cost")
if v1_h > 0:
    print(f"1 {v1_h:.2f} {v1_p:.2f}")
if v2_h > 0:
    print(f"2 {v2_h:.2f} {v2_p:.2f}")
print(f"Total {(v1_p+v2_p):.2f} THB")