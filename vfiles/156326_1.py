x = input("Enter a series of numbers separated by commas: ")
num = x.split(",")

# แปลงเป็น int ทีละตัว
num[0] = int(num[0])
num[1] = int(num[1])
num[2] = int(num[2])
num[3] = int(num[3])
num[4] = int(num[4])

# หา max
x_max = max(num)

# ตรวจสอบว่าเป็นค่าสูงสุดหรือไม่
r0 = (num[0] == x_max)
r1 = (num[1] == x_max)
r2 = (num[2] == x_max)
r3 = (num[3] == x_max)
r4 = (num[4] == x_max)

# แสดงผล
print(f"{num[0]} is the maximum value: {r0}")
print(f"{num[1]} is the maximum value: {r1}")
print(f"{num[2]} is the maximum value: {r2}")
print(f"{num[3]} is the maximum value: {r3}")
print(f"{num[4]} is the maximum value: {r4}"