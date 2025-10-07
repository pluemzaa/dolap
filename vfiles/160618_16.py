# รับข้อมูลจากผู้ใช้
nums = input("Enter a series of numbers separated by commas: ")
nums = nums.split(",")

# แปลงเป็นตัวเลข
nums = [float(n) for n in nums]

# หาค่าต่ำสุดและค่าสูงสุด
_min = min(nums)
_max = max(nums)

# คำนวณค่าที่ปรับช่วงแล้ว
print("Normalized values:")
for x in nums:
    x_scaled = (x - _min) / (_max - _min)
    print(f"{x_scaled:.2f}")