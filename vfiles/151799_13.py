v1 = input("Enter v1 (space-seperated): ")
v2 = input("Enter v2 (space-seperated): ")
hex_num1 = v1.split(" ")
hex_num2 = v2.split(" ")
hex_num1[0] = int(hex_num1[0])
hex_num2[0] = int(hex_num2[0])
hex_num1[1] = int(hex_num1[1])
hex_num2[1] = int(hex_num2[1])
hex_num1[2] = int(hex_num1[2])
hex_num2[2] = int(hex_num2[2])
A = hex_num1[0] * hex_num2[0]
B = hex_num1[1] * hex_num2[1]
C = hex_num1[2] * hex_num2[2]
D = A + B + C
print("Dot product :" ,D)