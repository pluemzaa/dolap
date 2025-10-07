v1 = input("Enter v1 (space-separated):")
v1 = v1.split('  ')
v1 = int(v1)
print(f"Enter v1 (space-separated):", {v1})


v2 = input("Enter v2 (space-separated):")
v2 = v2.split('  ')
v2 = int(v2)
print(f"Enter v1 (space-separated):", {v2})



a = (v1[0] * v2[0])
b = (v1[1] * v2[1])
c = (v1[2] * v2[2])

all = (a+b+c)
print(f"Dot Product:", {all})