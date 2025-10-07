num_dict = {"Dog" : [1, 0, 0] , "Cat" : [0, 1, 0] , "Fish" : [0, 0, 1]}
pet = input("Code of your pets:")

pet_str = input("Code of your pets number:")
pet_num = pet_str.split(",")

print("Result : ",end="\n")
print(num_dict [pet_num[0]] ,
      num_dict [pet_num[1]] ,
      num_dict [pet_num[2]] , sep="\n" )