ani = {"Dog": 0,"Cat": 1,"Fish": 2}
ani_input = input("Enter your pets: ")
ani_list = ani_input.split(",")
code1 = str(ani[ani_list[0]])
code2 = str(ani[ani_list[1]])
code3 = str(ani[ani_list[2]])
code4 = str(ani[ani_list[3]])
code5 = str(ani[ani_list[4]])
print("Code of your pets:", code1 + "," + code2 + "," + code3 + "," + code4 + "," + code5)