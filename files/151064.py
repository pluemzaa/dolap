v1 = input("Enter v1 (space-separated): ")
v2 = input("Enter v2 (space-separated): ")

v1_spl = v1.split()
v2_spl = v2.split()

print("Dot product:",
int(v1_spl[0]) * int(v2_spl[0]) + int(v1_spl[1]) * int(v2_spl[1]) + int(v1_spl[2]) * int(v2_spl[2])
)