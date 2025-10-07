Animal_name = input("Enter your pets: ")
Animal_list = Animal_name.split(",")

CodeAnimal = {"Dog": 0, "Cat": 1, "Fish": 2}
AllA = CodeAnimal[Animal_list[0]], CodeAnimal[Animal_list[1]],CodeAnimal[Animal_list[2]],CodeAnimal[Animal_list[3]],CodeAnimal[Animal_list[4]]
#print("Code of your pets: ", list(AllA))
A= list(AllA)

# AllA1 = AllA.split("\t")
# print("Code of your pets: ", AllA1)

print("Code of your pets: " ,A[0], A[1], A[2], A[3], A[4], sep=",")
#Dog,Cat,Fish,Cat,Dog