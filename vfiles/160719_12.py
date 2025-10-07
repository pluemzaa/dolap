records = []
total_price = 0.0

while True:
    t = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
    h = input("Please enter the number of parking hours: ")

    if not (t.replace(".", "", 1).isdigit() and h.replace(".", "", 1).isdigit()):
        print("Invalid input. Please enter numbers only.")

    else:
        t = float(t)
        h = float(h)
        price = 0.0

        if t != 1 and t != 2:
            print("Invalid vehicle type")

        elif h <= 0:
            print("Please enter a valid number of parking hours")

        else:

            if h < 1:
                price = 0.0

            elif t == 1:
                price = 10 + (h - 1) * 5

            elif t == 2:
                price = 30 + (h - 1) * 15

            print(f"Parking fee: {price:.2f} THB")
            records.append((int(t), h, price))
            total_price += price

    cont = input("Do you want to continue? (y/n): ")
    print("------------------------------")

    if cont != "y":
        break

print("VT Hours Cost")
for rec in records:
    print(f"{rec[0]} {rec[1]:.2f} {rec[2]:.2f}")
print(f"Total {total_price:.2f} THB")