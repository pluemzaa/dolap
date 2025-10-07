v1 = input("Enter v1 (space-separated): ")
v2 = input("Enter v2 (space-separated): ")

v_1 = v1.split(" ")
v_2 = v2.split(" ")

for i in range(0,3):
  v_1[i] = int(v_1[i])
  v_2[i] = int(v_2[i])
print(f"Dot product: {v_1[0]*v_2[0] + v_1[1]*v_2[1] + v_1[2]*v_2[2]}")