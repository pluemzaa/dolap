v1 = input("Enter v1 (space-separated):").split()
v1_list = list(map(int,v1))

v2 = input("Enter v2 (space-separated):").split()
v2_list = list(map(int,v2))

sum = v1_list[0]*v2_list[0] + v1_list[1]*v2_list[1] + v1_list[2]*v2_list[2]

print("Dot product:",sum)