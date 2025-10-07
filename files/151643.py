pets = input("Enter your pets:")
pets_num = {"Dog":0,"Cat":1,"Fish":2}
pets_word = pets
p = pets_word.split(',')
print("Code of your pets:",end=' ')
print(pets_num[p[0]],',',pets_num[p[1]],',',pets_num[p[2]],',',pets_num[p[3]],',',pets_num[p[4]],sep='')

pets_num1 = {"Dog":[1, 0, 0],"Cat":[0, 1, 0],"Fish":[0, 0, 1]}
pets_word1 = pets
p1 = pets_word1.split(',')
print("One-hot vectors:",end='\n')
print(pets_num1[p1[0]],'\n',pets_num1[p1[1]],'\n',pets_num1[p1[2]],'\n',pets_num1[p1[3]],'\n',pets_num1[p1[4]],sep='')