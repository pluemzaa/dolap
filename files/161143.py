ca = 0.00
hc = 0.00
m = 0.00
hm = 0.00

while True:
    v = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    h = float(input("Please enter the number of parking hours: "))

    if v not in [1, 2]:
        print("Invalid vehicle type")
    elif h <= 0:
        print("Please enter a valid number of parking hours")
    else:
        if v == 1 and h < 1:  
            print(f"Parking fee: 0.00 THB")
            hm += h
        elif v == 2 and h < 1:
            print(f"Parking fee: 0.00 THB")
            hc += h
        elif v == 1:
            c = 5
            p = 10 + ((h-1)*c)
            print(f"Parking fee: {p:.2f} THB")  
            m += p
            hm += h            
        elif v == 2:
            c = 15
            p = 30 + ((h-1)*c)
            print(f"Parking fee: {p:.2f} THB")
            ca += p
            hc += h 
    cont = input("Do you want to continue? (y/n): ")
    if cont == "y":
        print("------------------------------")
    elif cont == "n":
        break

print("------------------------------")
print("VT Hours Cost")
if hm > 0:
    print(f"1 {hm:.2f} {m:.2f}")
if hc > 0:
    print(f"2 {hc:.2f} {ca:.2f}")
print(f"Total {ca + m:.2f} THB")