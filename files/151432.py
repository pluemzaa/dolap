pet_dict = {"Dog":0,"Cat":1,"Fish":2}
pet_text = input("Enter your pets:")
p = pet_text.split(",")
print("Code of your pets:",end="")
print(pet_dict[p[0]],pet_dict[p[1]],pet_dict[p[2]],pet_dict[p[3]],pet_dict[p[4]],sep=",")