pet_txt = input("Enter your pets: ")  # เช่น Dog,Cat,Dog,Fish,Cat
g = pet_txt.split(",")

pet_num = {"Dog": 0, "Cat": 1, "Fish": 2}

print(pet_num[g[0]], ",", pet_num[g[1]], ",", pet_num[g[2]], ",", pet_num[g[3]], ",", pet_num[g[4]], sep="")