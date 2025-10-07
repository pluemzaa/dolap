nums_text = input('Enter a series of numbers separated by commas:')
nums = nums_text.split(",")
x_min = min(nums)
x_max = max(nums)
nums[0] = int (nums[0])
nums[1] = int (nums[1])
nums[2] = int (nums[2])
nums[3] = int (nums[3])
nums[4] = int (nums[4])
r0 = nums[0]- x_min/x_max-x_min
r1 = nums[1]- x_min/x_max-x_min
r2 = nums[2]- x_min/x_max-x_min
r3 = nums[3]- x_min/x_max-x_min
r4 = nums[4]- x_min/x_max-x_min
r5 = nums[5]- x_min/x_max-x_min
print("%.2f" % r0)
print("%.2f" % r1)
print("%.2f" % r2)
print("%.2f" % r3)
print("%.2f" % r4)
print("%.2f" % r5)
# รับข้อมูล 5 ค่า จากผู้ใช้
x1 = float(input("ป้อนค่าลำดับที่ 1: "))
x2 = float(input("ป้อนค่าลำดับที่ 2: "))
x3 = float(input("ป้อนค่าลำดับที่ 3: "))
x4 = float(input("ป้อนค่าลำดับที่ 4: "))
x5 = float(input("ป้อนค่าลำดับที่ 5: "))

# รวมข้อมูลไว้ใน list
data = [x1, x2, x3, x4, x5]

# หาค่า min และ max
min_value = min(data)
max_value = max(data)

# ทำ Min-Max Normalization ทีละตัว (ไม่ใช้ loop)
x1_scaled = (x1 - min_value) / (max_value - min_value)
x2_scaled = (x2 - min_value) / (max_value - min_value)
x3_scaled = (x3 - min_value) / (max_value - min_value)
x4_scaled = (x4 - min_value) / (max_value - min_value)
x5_scaled = (x5 - min_value) / (max_value - min_value)

# แสดงผลลัพธ์
print("ข้อมูลหลังการปรับช่วงให้อยู่ในช่วง [0, 1]:")
print([x1_scaled, x2_scaled, x3_scaled, x4_scaled, x5_scaled])