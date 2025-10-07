H_m = 0
H_c = 0
p_m = 0
p_c = 0
while True:
    v = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
    T = float(input("Please enter the number of parking hours: "))
    if v not in ["1","2"]:
        print("Invalid vehicle type")
        pass 
    elif T <= 0:
        print("Please enter a valid number of parking hours")
        pass
    elif v == "1":
        H_m += T 
        if T < 1:
            p = 0
        elif T >= 1:
            p = 10 + ((T-1)*5)
        p_m += p
        print(f'Parking fee: {p:.2f} THB')    
    elif v == "2":
        H_c += T
        if T < 1:
            p = 0
        elif T >= 1:
            p = 30 + ((T-1)*15)
        p_c += p
        print(f'Parking fee: {p:.2f} THB')     
    D = input("Do you want to continue? (y/n): ")
    print("------------------------------")
    if D == 'y':
        continue
    elif D == 'n':
        break 
    
print("VT Hours Cost")
if H_m > 0:
    print(f"1 {H_m:.2f} {p_m:.2f}")
if H_c > 0:
    print(f"2 {H_c:.2f} {p_c:.2f}")
print(f"Total {(p_m + p_c):.2f} THB")