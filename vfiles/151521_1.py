Animal_name = input("Enter your pets: ")
Animal_list = Animal_name.split(",")
# print(Animal_list)

CodeAnimal = {"Dog":0, "Cat":1, "Fish":2}


print("Code of your pets: ",CodeAnimal[Animal_list[0]],",", CodeAnimal[Animal_list[1]],",",CodeAnimal[Animal_list[2]],",", CodeAnimal[Animal_list[3]],",", CodeAnimal[Animal_list[4]], sep="")

CodeAnimal1 = {"Dog":[1, 0, 0], "Cat":[0, 1, 0], "Fish":[0, 0, 1]}
print("One-hot vectors:\n",CodeAnimal1[Animal_list[0]],"\n", CodeAnimal1[Animal_list[1]],"\n",CodeAnimal1[Animal_list[2]],"\n", CodeAnimal1[Animal_list[3]],"\n", CodeAnimal1[Animal_list[4]], sep="")


#Dog,Cat,Fish,Dog,Fish