pet_name= {"Dog":0,"Cat":1,"Fish":2}
pet_sec = {0:[1,0,0],1:[0,1,0],2:[0,0,1]}
pet_str = input("Enter your pets:")
pets = [pet.strip() for pet in input_str.split(',')]

if len(pets) !=5:
    print("Error: Please enter exactly 5 pets names.")

else:
    codes = [pet_name[pet]for pet in pets]

print("Code of your pets:",",".join(map(str,codes)))

print("One-hot vectors:")

for code in codes:
    print(pet_sec[code])