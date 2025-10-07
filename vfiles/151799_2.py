v1 = input("Enter v1 (space-seperated)")
v2 = input("Enter v2 (space-seperated)")
hex_num1 = v1.split(" ")
hex_num2 = v2.split(" ")
hex_num1[0] = int(hex_num1[0])
hex_num2[0] = int(hex_num2[0])
hex_num1[1] = int(hex_num1[1])
hex_num2[1] = int(hex_num2[1])
hex_num1[2] = int(hex_num1[2])
hex_num2[2] = int(hex_num2[2])
G = hex_num1[0] * hex_num2[0]
O = hex_num1[1] * hex_num2[1]
D = hex_num1[2] * hex_num2[2]
Z = G + O + D
print("Dot product:" ,Z)