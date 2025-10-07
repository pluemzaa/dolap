grade_num = {"Dog":[1,0,0], "Cat":[0,1,0],"Fish":[0,0,1]}
grade_text = "Dog,Cat,Fish"
# 4,4,3.5,0
g = grade_text.split(",")
print(g)
print("result:",end=" ")
print(grade_num[g[0]],",",grade_num[g[1]],",",grade_num[g[0]],",",grade_num[g[2]],",",grade_num[g[1]],end=" ")