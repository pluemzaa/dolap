pet = input("Enter your pets:")
print(pet)
pet_num = {'Dog' : 0,'Cat' : 1,'Fish' : 2}
pet_text = "Dog,Cat,Dog,Fish,Cat"
p = pet_text.split(",")
pet_c = pet_num['Dog'],pet_num['Cat'],pet_num['Dog'],pet_num['Fish'],pet_num['Cat']
print("Code of your pets:", pet_c)