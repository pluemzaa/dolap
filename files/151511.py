animal_dict = {"Dog":0, "Cat":1, "Fish":2}
one_hot_dict = {"Dog": [1,0,0],"Cat": [0,1,0],"Fish": [0,0,1]}

animal_input = input("Enter your pets: ")

animal = [pet.strip() for pet in animal_input.split(",")]

codes = [str(animal_dict[pet]) for pet in animal]
print("Code of your pets:", ",".join(codes))
print("One-hot vectors:")
for pet in animal:
 print(one_hot_dict[pet])