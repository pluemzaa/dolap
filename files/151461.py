# dog = 0
# cat = 1
# fish = 2

animal = {"Dog":0, "Cat":1,"Fish": 2}
pet_str = input("Enter your pets:")
am = pet_str.split(",")
print("Code of your pets:",end="")
print(animal[am[0]],animal[am[1]],animal[am[2]],animal[am[3]],animal[am[4]],sep=",")