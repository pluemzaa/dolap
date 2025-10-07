# รับอินพุตจากผู้ใช้
numbers_str = input("Enter a series of numbers separated by commas: ")

# แยกสตริงเป็นลิสต์ของสตริง จากนั้นแปลงเป็นลิสต์ของจำนวนเต็ม
numbers = [int(num) for num in numbers_str.split(',')]

# หาค่าสูงสุดของตัวเลขทั้งหมด
maximum_value = max(numbers)

# วนลูปเพื่อตรวจสอบและแสดงผลสำหรับแต่ละตัวเลข
for num in numbers:
    # ใช้ comparison operator (==) เพื่อเปรียบเทียบว่าตัวเลขปัจจุบันเท่ากับค่าสูงสุดหรือไม่
    # ผลลัพธ์จะเป็น True หรือ False โดยตรง
    is_maximum = (num == maximum_value)
    print(f"{num} is the maximum value: {is_maximum}")