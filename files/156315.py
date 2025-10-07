# รับค่าตัวเลขจากผู้ใช้และแปลงเป็น list ของจำนวนเต็ม
numbers = list(map(int, input("Enter a series of numbers separated by commas: ").split(',')))

# หาค่าสูงสุดจากลิสต์
max_value = max(numbers)

# ตรวจสอบและแสดงผลว่าแต่ละค่าคือค่าสูงสุดหรือไม่
results = [(str(n) + " is the maximum value: " + str(n == max_value)) for n in numbers]

# แสดงผลลัพธ์
print('\n'.join(results))