mc = 0.00
mh = 0.00
cc = 0.00
ch = 0.00

while True:
    f = 0.0
    
    v_in = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car):").strip()
    h_in = input("Please enter the number of parking hours:").strip()

    is_valid = (
        h_in.replace('.', '', 1).isdigit() and
        h_in.count('.') <= 1 and
        (h_in[0] != '-' or h_in == "0")
    )

    if not v_in.isdigit() or int(v_in) not in [1, 2]:
        print("Invalid vehicle type")
        continue

    if not is_valid:
        print("Please enter a valid number of parking hours")
        continue

    v = int(v_in)
    h = float(h_in)

    if h <= 0:
        print("Please enter a valid number of parking hours")
        continue

    if h < 1:
        f = 0.0
    elif v == 1:
        f = 10 + (h - 1) * 5
    else:
        f = 30 + (h - 1) * 15

    print(f"Parking fee: {f:.2f} THB")

    if v == 1:
        mc += f
        mh += h
    else:
        cc += f
        ch += h

    cont = input("Do you want to continue? (y/n):").strip().lower()
    print("------------------------------")
    if cont != 'y':
        break

print("\nVT Hours Cost")
print(f"1 {mh:.2f} {mc:.2f}")
print(f"2 {ch:.2f} {cc:.2f}")
print(f"Total {mc + cc:.2f}")