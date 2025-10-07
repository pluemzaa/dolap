num_dict = {"Dog":0, "Cat":1, "Fish":2}

pet = input("Enter your pets: ")
pet = pet.split(",")

print("Code of your pets:", end='')
print(num_dict[pet[0]],num_dict[pet[1]],num_dict[pet[2]],num_dict[pet[3]],num_dict[pet[4]],sep=',')