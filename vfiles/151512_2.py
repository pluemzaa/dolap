Animal_name = input("Enter your pets: ")
Animal_list = Animal_name.split(",")

CodeAnimal = {"Dog": "0", "Cat": "1", "Fish": "2"}
print("Code of your pets: ", CodeAnimal[Animal_list[0]], CodeAnimal[Animal_list[1]],CodeAnimal[Animal_list[2]],CodeAnimal[Animal_list[3]],CodeAnimal[Animal_list[4]])