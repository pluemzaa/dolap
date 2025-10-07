pet_str = input("Enter your pets: ")
pet_code = { "Dog" : 0, "Cat" : 1, "Fish" : 2}

vecter_pet_code = {"Dog": [1,0,0], "Cat": [0,1,0], "Fish": [0,0,1]}

s = pet_str.split(",") 
c1 = pet_code[s[0]]
c2 = pet_code[s[1]]
c3 = pet_code[s[2]]
c4 = pet_code[s[3]]
c5 = pet_code[s[4]]
print(f"Code of your pets: {c1},{c2},{c3},{c4},{c5}")
print("One-hot vectors:")
print(vecter_pet_code[s[0]])
print(vecter_pet_code[s[1]])
print(vecter_pet_code[s[2]])
print(vecter_pet_code[s[3]])
print(vecter_pet_code[s[4]])