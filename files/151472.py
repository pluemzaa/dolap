ani = {"Dog": 0,"Cat": 1,"Fish": 2}
ani_2 = {"Dog": [1, 0, 0],"Cat": [0, 1, 0],"Fish": [0, 0, 1]}
ani_input = input("Enter your pets: ")
ani_list = ani_input.split(",")

code1 = str(ani[ani_list[0]])
code2 = str(ani[ani_list[1]])
code3 = str(ani[ani_list[2]])
code4 = str(ani[ani_list[3]])
code5 = str(ani[ani_list[4]])

One_code_1 = str(ani_2[ani_list[0]])
One_code_2 = str(ani_2[ani_list[1]])
One_code_3 = str(ani_2[ani_list[2]])
One_code_4 = str(ani_2[ani_list[3]])
One_code_5 = str(ani_2[ani_list[4]])

print("Code of your pets:", code1 + "," + code2 + "," + code3 + "," + code4 + "," + code5)

print("one-hot vectors:\n", One_code_1 + "\n" + One_code_2 + "\n" + One_code_3 + "\n" + One_code_4 + "\n" + One_code_5)