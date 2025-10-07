pet_num = {'Dog' :0,'Cat' : 1,'Fish':2}
pet_text=input("Enter your pets:")
p=pet_text.split(",")
print("Code of your pets:",pet_num[p[0]],",",pet_num[p[1]],",",pet_num[p[2]],",",pet_num[p[3]],",",pet_num[p[4]])