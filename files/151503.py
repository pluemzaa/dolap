pets_dict = {"Dog":"0","Cat":"1","Fish":"2"}
pets_str = input("Enter your pets: ")
pets_num = pets_str.split(",")

p1 = pets_num[0]
p2 = pets_num[1]
p3 = pets_num[2]
p4 = pets_num[3]
p5 = pets_num[4]

num1 = pets_dict[p1]
num2 = pets_dict[p2]
num3 = pets_dict[p3]
num4 = pets_dict[p4]
num5 = pets_dict[p5]

pX = num1+","+num2+","+num3+","+num4+","+num5

print("Code of your pets: ",pX)
print("One-hot vectors:" )
numX = ["[1, 0, 0]","[0, 1, 0]","[0, 0, 1]"]
print(numX[int(num1)])
print(numX[int(num2)])
print(numX[int(num3)])
print(numX[int(num4)])
print(numX[int(num5)])