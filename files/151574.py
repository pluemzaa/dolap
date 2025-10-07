name = input("Enter your name: ")
mail = input("Enter your email: ")
gpa = input("Enter your GPA: ")

gpa = float(gpa)

lit = [name,mail,gpa]
tup = (name,mail,gpa)
dic = {"name":name,"email":mail,"GPA":gpa}


print(lit)
print(tup)
print(dic)