x = []

while True:
    vc = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
    hr = float(input("Please enter the number of parking hours: "))

    if hr <= 0:
        print("Please enter a valid number of parking hours")
        again = input("Do you want to continue? (y/n): ")
        print("------------------------------")
        if again != "y":
            break
        continue

    if hr < 1:
        price = 0.00
    elif vc == "1":
        price = 10 + (hr - 1) * 5
    elif vc == "2":
        price = 30 + (hr - 1) * 15
    else:
        print("Invalid vehicle type")
        again = input("Do you want to continue? (y/n): ")
        print("------------------------------")
        if again != "y":
            break
        continue

    print(f"Parking fee: {price:.2f} THB")
    x.append((vc,hr,price))

    again = input("Do you want to continue? (y/n): ")
    print("------------------------------")
    if again != "y":
        break

print("VT Hours Cost")
total = 0
for entry in x:
    vt, hrs,cost = entry
    print(f"{vt} {hrs:.2f} {cost:.2f}")
    total += cost
print(f"Total {total:.2f} THB")