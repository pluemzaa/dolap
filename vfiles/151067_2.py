v1 = input("Enter v1 (space-separated): ")
v2 = input("Enter v2 (space-separated): ")

v_1 = v1.split(" ")
v_2 = v2.split(" ")

for i in range(3):
    v_1[i] = int(v_1[i])
    v_2[i] = int(v_2[i])
print(f"Dot product: {v1s[0]*v2s[0] + v1s[1]*v2s[1] + v1s[2]*v2s[2]}")