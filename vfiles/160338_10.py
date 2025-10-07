# รับตัวเลขแยกด้วยคอมม่า
n = input("Enter numbers separated by commas: ").split(",")
n = [int(x.strip()) for x in n]

# รับค่าที่จะค้นหา
y = int(input("Enter number to search: "))

# ค้นหาและแสดงผล
found = False
for i in range(len(n)):
    if n[i] == y:
        print(f"Found {y} at index {i}")
        found = True

if not found:
    print(f"No {y} found")