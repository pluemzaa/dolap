v1_price = 0
v2_price = 0
h1_sum = 0
h2_sum = 0
records = []

while True:
    v = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car):"))
    h = float(input("Please enter the number of parking hours:"))

    if v not in [1, 2]:
        print("Invalid vehicle type")
        con = input("Do you want to continue? (y/n):")
        print("------------------------------")
        if con == 'n':
            break
        else:
            continue

    if h <= 0:
        print("Please enter a valid number of parking hours")
        con = input("Do you want to continue? (y/n):")
        print("------------------------------")
        if con == 'n':
            break
        else:
            continue


    if h < 1:
        fee = 0.00
    else:
        if v == 1:
            fee = 10 + (h - 1) * 5
        else:
            fee = 30 + (h - 1) * 15

    print(f"Parking fee: {fee:.2f} THB")


    records.append((v, h, fee))
    if v == 1:
        h1_sum += h
        v1_price += fee
    else:
        h2_sum += h
        v2_price += fee

    con = input("Do you want to continue? (y/n):")
    print("------------------------------")
    if con == 'n':
        break


print("VT Hours Cost")
if v1_price > 0 or h1_sum > 0:
    print(f"1 {h1_sum:.2f} {v1_price:.2f}")
if v2_price > 0 or h2_sum > 0:
    print(f"2 {h2_sum:.2f} {v2_price:.2f}")
print(f"Total {v1_price+v2_price:.2f} THB")