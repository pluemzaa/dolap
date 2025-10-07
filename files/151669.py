pat_num = { "Dog": 0 , "Cat": 1 , "Fish": 2 }

pat_text = input("Enter your pets:")

p = pat_text.split(",")
print("code of your pets:", end='  ')
print(pat_num[p[0]],",",pat_num[p[1]],",", pat_num[p[2]],"," ,pat_num[p[3]],",", pat_num[p[4]], sep='')