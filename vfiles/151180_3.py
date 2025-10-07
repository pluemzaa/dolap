pet_names = ["Dog", "Cat", "Fish"]
pets_input = input("Enter your pets: ")
pets_list = pets_input.split(",")
code0 = pet_names.index(pets_list[0].strip())
code1 = pet_names.index(pets_list[1].strip())
code2 = pet_names.index(pets_list[2].strip())
code3 = pet_names.index(pets_list[3].strip())
code4 = pet_names.index(pets_list[4].strip())
print("Code of your pets:", str(code0) + "," + str(code1) + "," + str(code2) + "," + str(code3) + "," + str(code4))
one_hot0 = [0, 0, 0]
one_hot0[code0] = 1

one_hot1 = [0, 0, 0]
one_hot1[code1] = 1

one_hot2 = [0, 0, 0]
one_hot2[code2] = 1

one_hot3 = [0, 0, 0]
one_hot3[code3] = 1

one_hot4 = [0, 0, 0]
one_hot4[code4] = 1
print("One-hot vectors:")
print(one_hot0)
print(one_hot1)
print(one_hot2)
print(one_hot3)
print(one_hot4)