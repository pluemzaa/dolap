v1_text = input("Enter v1 (space-separated):")
v1_parts = v1_text.split()
v2_text = input("Enter v2 (space-separated):")
v2_parts = v2_text.split()

num1_v1 = int(v1_parts[0])
num1_v2 = int(v2_parts[0])
sum1 = num1_v1 * num1_v2

num2_v1 = int(v1_parts[1])
num2_v2 = int(v2_parts[1])
sum2 = num2_v1 * num2_v2

num3_v1 = int(v1_parts[2])
num3_v2 = int(v2_parts[2])
sum3 = num3_v1 * num3_v2

dot_product = sum1 + sum2 + sum3
print(f"Dot product: {dot_product}")