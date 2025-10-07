# รับตัวเลขจากผู้ใช้ แยกด้วย comma แล้วแปลงเป็นจำนวนเต็ม
nums = input("Enter a series of numbers separated by commas: ")
nums_list = [int(x.strip()) for x in nums.split(",")]

# หา maximum value ใน list
maximum = max(nums_list)

# แสดงผลลัพธ์โดยใช้ comparison operators และ logical operators โดยไม่ใช้ if
for n in nums_list:
    print(f"{n} is the maximum value: {n == maximum}")