grade_num = {"Dog": 0 , "Cat": 1 , "Fish": 2 }
grade_ver = {"Dog":[1,0,0], "Cat":[0,1,0], "Fish":[0,0,1]}

grade_text = input("Enter your pets :")

g = grade_text.split(",")
print("Code of your pets:", end=' ')
print(grade_num[g[0]],",",grade_num[g[1]],",",grade_num[g[2]],",",grade_num[g[3]],",",grade_num[g[4]],sep='')
print("One-hot vectors:")

print(grade_ver[g[0]])
print(grade_ver[g[2]])
print(grade_ver[g[0]])
print(grade_ver[g[3]])
print(grade_ver[g[1]])