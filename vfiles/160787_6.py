time = 0
fee = 0
car = 0
records = []
total_fee = 0  

while True:
    car = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    if car != 1 and car != 2:
        print("Invalid vehicle type, please enter 1 for Motorcycle or 2 for Personal Car.")
        continue

    time = float(input("Please enter the number of parking hours: "))
    
    if time < 0:
        print("Please enter a valid number of parking hours")
        continue  

    if time < 1:
        fee = 0.00  
    else:
        if car == 1:
            if time == 1:
                fee = 10
            else:
                fee = 10 + (time - 1) * 5
        elif car == 2:
            if time == 1:
                fee = 30
            else:
                fee = 30 + (time - 1) * 15

    print(f"Parking fee: {fee:.2f} THB")
    
    records.append((car, time, fee))
    total_fee += fee  

    
    continue_choice = input("Do you want to continue? (y/n): ").lower()
    if continue_choice == 'n':
       
        print("\nVT Hours Cost")
        for record in records:
            print(f"{record[0]}  {record[1]:.2f}  {record[2]:.2f}")

        print(f"Total {total_fee:.2f} THB")
        break  
    elif continue_choice != 'y':
        print("Invalid input, please enter 'y' or 'n'.")
        continue