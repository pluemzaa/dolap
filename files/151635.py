# a => 4
# b+ => 3.5
# b => 3
# f => 0
grade_num = { "Dog": 0, "Cat": 1, "Fish": 2 }

grade_text = input("Enter your pets:")
# 4,4,3,5,0
g = grade_text.split(",")
print("Code of your pets:", end=' ')
print(grade_num[g[0]], ",", grade_num[g[1]], ",",grade_num[g[2]], ",",grade_num[g[3]], ",",grade_num[g[4]], sep='')