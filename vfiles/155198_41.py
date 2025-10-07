# รับอินพุตจากผู้ใช้
numbers_str = input("Enter a series of numbers separated by commas: ")

# แยกสตริงและแปลงเป็นลิสต์ของจำนวนเต็ม
# List comprehension นี้จะช่วยให้โค้ดกระชับขึ้น
numbers = [int(num) for num in numbers_str.split(',')]

# หาค่าสูงสุดจากลิสต์ตัวเลข
maximum_value = max(numbers)

# วนลูปผ่านแต่ละตัวเลขเพื่อตรวจสอบและแสดงผล
for num in numbers:
    # ใช้ Comparison operator (==) เพื่อเปรียบเทียบตัวเลขปัจจุบันกับค่าสูงสุด
    # ผลลัพธ์ของการเปรียบเทียบจะเป็น True หรือ False ทันที
    is_maximum = (num == maximum_value)
    print(f"{num} is the maximum value: {is_maximum}")