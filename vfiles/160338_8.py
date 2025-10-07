# รับค่าตัวเลขคั่นด้วย ,
n = input("Enter numbers separated by commas: ")
n = n.split(",")
n = [int(x.strip()) for x in n]  # แปลงเป็น int ทุกตัวและลบช่องว่าง

# รับค่าที่จะค้นหา
y = int(input("Enter number to search: "))

# ค้นหา
found = False
for i in range(len(n)):
    if n[i] == y:
        print(f"Found {y} at index {i}")
        found = True

if not found:
    print(f"No {y} found")