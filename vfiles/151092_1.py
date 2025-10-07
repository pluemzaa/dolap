# A => 4
# B+ => 3.5
# B => 3
# F => 0

grade_num = {"A":[0,0,0,1], "B+":[0,0,1,0], "B":[0,1,0,0], "f" :[1,0,0,0]}

grade_text = "A,A,B+,F"
#4,4,3.5,0
g = grade_text.split(",")
print(g)
print("Result:",end=' ')
print(grade_num[g[0]],",",grade_num[g[1]],sep='')