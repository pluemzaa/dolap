v1_input = input("Enter v1 (space-separated):")
v1 = list(map(int, v1_input.strip().split()))
v2_input = input("Enter v2 (space-separated):")
v2 = list(map(int, v2_input.strip().split()))
dot_product = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]