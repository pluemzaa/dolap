nums = input("Enter numbers separated by commas: ")
nums = nums.split(",")
x = int(input("Enter number to search: "))

# แปลงค่าทั้งหมดในลิสต์เป็น int
for i in range(len(nums)):
    nums[i] = int(nums[i])

found = False  # ตัวแปรช่วยเช็คว่ามีเจอหรือไม่

# ค้นหาค่าในลิสต์
for i in range(len(nums)):
    if x == nums[i]:
        print(f"Found {x} at index {i}")
        found = True

# ถ้าไม่เจอเลย
if not found:
    print(f"No {x} found.")