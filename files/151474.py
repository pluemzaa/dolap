ani = {"Dog": 0, "Cat": 1, "Fish": 2}
onehot = {"Dog": "[1, 0, 0]", "Cat": "[0, 1, 0]", "Fish": "[0, 0, 1]"}
ani_input = input("Enter your pets: ")
ani_list = ani_input.split(",")

code1 = str(ani[ani_list[0].strip()])
code2 = str(ani[ani_list[1].strip()])
code3 = str(ani[ani_list[2].strip()])
code4 = str(ani[ani_list[3].strip()])
code5 = str(ani[ani_list[4].strip()])

print("Code of your pets:", code1 + "," + code2 + "," + code3 + "," + code4 + "," + code5)
print("One-hot vectors:")
print(onehot[ani_list[0].strip()])
print(onehot[ani_list[1].strip()])
print(onehot[ani_list[2].strip()])
print(onehot[ani_list[3].strip()])
print(onehot[ani_list[4].strip()])