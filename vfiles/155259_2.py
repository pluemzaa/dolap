input_str = input("Enter a series of numbers separated by commas: ")

# แปลงข้อความเป็นลิสต์ของจำนวนเต็ม
numbers = [float(x.strip()) for x in input_str.split(",")]

# ตรวจสอบว่าได้รับข้อมูล 5 ตัวหรือไม่ (ถ้าจำเป็น)
if len(numbers) != 5:
    print("Please enter exactly 5 numbers.")
else:
   
    min_val = min(numbers)
    max_val = max(numbers)

    
    if max_val == min_val:
        print("All values are the same. Normalized values will all be 0.00")
        normalized = [0.00 for _ in numbers]
    else:
        normalized = [(x - min_val) / (max_val - min_val) for x in numbers]

   
    print("Normalized values:")
    for val in normalized:
        print(f"{val:.2f}")