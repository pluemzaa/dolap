v1 = input("Enter v1 (space-separated): ")
v2 = input("Enter v2 (space-separated): ")

v_1 = v1.split(" ")
v_2 = v2.split(" ")

v_1[0] = int(v_1[0])
v_1[1] = int(v_1[1])
v_1[2] = int(v_1[2])

v_2[0] = int(v_2[0])
v_2[1] = int(v_2[1])
v_2[2] = int(v_2[2])
print(f"Dot product: {v_1[0]*v_2[0]+v_1[1]*v_2[1]+v_1[2]*v_2[2]}")