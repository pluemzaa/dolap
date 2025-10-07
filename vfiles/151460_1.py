num_dict = {"Dog": [1, 0, 0],"Cat": [0, 1, 0],"Fish": [0, 0, 1]}

hnum = input("Enter your pets: ") 
hnum = hnum.split(',')

pet0 = hnum[0].strip()
pet1 = hnum[1].strip()
pet2 = hnum[2].strip()
pet3 = hnum[3].strip()
pet4 = hnum[4].strip()

print("Code of your pets:", end='\n')
print(list(num_dict.keys()).index(pet0),list(num_dict.keys()).index(pet1),list(num_dict.keys()).index(pet2),list(num_dict.keys()).index(pet3),list(num_dict.keys()).index(pet4),sep=',')

print("One-hot vectors:")
print(num_dict[pet0])
print(num_dict[pet1])
print(num_dict[pet2])
print(num_dict[pet3])
print(num_dict[pet4])