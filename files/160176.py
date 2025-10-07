# รับค่าตัวเลข คั่นด้วยลูกน้ำ แปลงเป็นลิสต์ของ int
nums = input("Enter numbers separated by commas: ")
num_list = [int(x.strip()) for x in nums.split(",")]

# รับค่าที่ต้องการค้นหา
search_num = int(input("Enter number to search: "))

# ค้นหาค่าที่ต้องการในลิสต์
found = False
for i, num in enumerate(num_list):
    if num == search_num:
        print(f"Found {search_num} at index {i}")
        found = True

if not found:
    print(f"No {search_num} found.")