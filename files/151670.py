pat_num = { "Dog": 0 , "Cat": 1 , "Fish": 2 }
pat_num2 = {"Dog":[1,0,0], "Cat":[0,1,0], "Fish":[0,0,1]}

pat_text = input("Enter your pets:")

p = pat_text.split(",")
print("code of your pets:", end='  ')
print(pat_num[p[0]],",",pat_num[p[1]],",", pat_num[p[2]],"," ,pat_num[p[3]],",", pat_num[p[4]], sep='')

print("One-hot vectors:")
print(pat_num2[p[0]])
print(pat_num2[p[1]])
print(pat_num2[p[2]])
print(pat_num2[p[3]])
print(pat_num2[p[4]])