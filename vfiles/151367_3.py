pet = input("Enter your pets:")
pet_num = {'Dog':0,'Cat':1,'Fish':2}
p = pet.split(",")
pet_c = pet_num[p[0]],pet_num[p[1]],pet_num[p[2]],pet_num[p[3]],pet_num[p[4]]
print("Code of your pets:", pet_c,sep=',')