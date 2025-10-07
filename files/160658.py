r = []
while True:
    t = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
    try:
        h = float(input("Please enter the number of parking hours: "))
    except:
        print("Please enter a valid number of parking hours")
        c = input("Do you want to continue? (y/n): ").lower()
        print("-" * 30)
        if c != 'y':
            break
        continue
    if t not in ['1', '2']:
        print("Invalid vehicle type")
    elif h <= 0:
        print("Please enter a valid number of parking hours")
    else:
        if h < 1:
            f = 0.00
        elif t == '1':
            f = 10 + (h - 1) * 5
        else:
            f = 30 + (h - 1) * 15
        print(f"Parking fee: {f:.2f} THB")
        r.append((t, h, f))
    c = input("Do you want to continue? (y/n): ").lower()
    print("-" * 30)
    if c != 'y':
        break
print("VT Hours Cost")
s = 0
for v, m, z in r:
    print(f"{v} {m:.2f} {z:.2f}")
    s += z
print(f"Total {s:.2f} THB")