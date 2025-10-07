nums_str = input("Enter a series of numbers separated by commas: ")
nums = [float(x.strip()) for x in nums_str.split(",")]

if len(nums) != 5:
    print("กรุณาใส่ข้อมูล 5 ตัวเท่านั้น")
    exit()

x_min = min(nums)
x_max = max(nums)

print("Normalized values:")

# ตรวจเงื่อนไขกรณี max == min เพื่อหลีกเลี่ยงหารด้วย 0
if x_max == x_min:
    for _ in nums:
        print(f"{0.00:.2f}")
else:
    for x in nums:
        x_norm = (x - x_min) / (x_max - x_min)
        print(f"{x_norm:.2f}")