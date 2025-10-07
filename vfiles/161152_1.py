park_data = []

while True:
    v = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car):"))
    h = float(input("Please enter the number of parking hours:"))
    if v == 1 or v == 2:
        if h > 0:
            fee = 0.0
            if h < 1:
                fee = 0.0
            elif v == 1:
                fee = 10 + (h - 1) * 5
            elif v == 2:
                fee = 30 + (h - 1) * 15
            print(f"Parking fee: {fee:.2f} THB")
            park_data.append({'v': v, 'h': h, 'fee': fee})  # บันทึกข้อมูล
        else:
            print("Please enter a valid number of parking hours")
    else:
        print("Invalid vehicle type")

    con = input('Do you want to continue? (y/n):')
    if con.lower() == 'n':
        print('------------------------------')
        break
    print('------------------------------')

if park_data:
    print("VT Hours Cost")
    total = 0
    for item in park_data:
        print(f"{item['v']} {item['h']:.2f} {item['fee']:.2f}")
        total += item['fee']
    print(f"Total {total:.2f} THB")