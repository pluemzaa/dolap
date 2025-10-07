# รับตัวเลขกี่ตัวก็ได้จากผู้ใช้
numbers = list(map(int, input("Enter a series of numbers separated by commas: ").split(',')))

# หาค่าสูงสุด
maximum = max(numbers)

# ใช้ list comprehension + print (ไม่ใช่ for loop ปกติ)
[print(f"{n} is the maximum value: {n == maximum}") for n in numbers]")