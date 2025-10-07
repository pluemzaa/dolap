def calculate_fee(vehicle_type, hours):
    if hours < 1:
        return 0.0
    if vehicle_type == 1:  # Motorcycle
        fee = 10 + (hours - 1) * 5
    elif vehicle_type == 2:  # Personal Car
        fee = 30 + (hours - 1) * 15
    else:
        fee = None
    return fee

def main():
    records = []
    record_number = 1
    total_fee = 0.0
    
    while True:
        try:
            vehicle_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
            if vehicle_type not in [1, 2]:
                print("Invalid vehicle type")
                break
            
            hours = float(input("Please enter the number of parking hours: "))
            if hours <= 0:
                print("Please enter a valid number of parking hours")
                break
            
            fee = calculate_fee(vehicle_type, hours)
            print(f"Parking fee: {fee:.2f} THB")
            
            # บันทึกเฉพาะรายการที่ถูกต้อง
            records.append((vehicle_type, hours, fee))
            total_fee += fee
            
            cont = input("Do you want to continue? (y/n): ").strip().lower()
            print("------------------------------")
            if cont != 'y':
                break
            
        except ValueError:
            # กรณีป้อนข้อมูลผิดพลาด เช่น ตัวหนังสือ
            print("Invalid input, program will exit.")
            break
    
    # สรุปรายการและค่าจอดรถรวม
    if records:
        print("VT Hours Cost")
        for vt, hr, cost in records:
            print(f"{vt} {hr:.2f} {cost:.2f}")
        print(f"Total {total_fee:.2f} THB")

if __name__ == "__main__":
    main()