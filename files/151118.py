name = input("Enter your name: ")
email = input("Enter your email: ")
gpa = float(input("Enter your GPA: "))

data_list = [name,email,gpa]
data_tuple = (name,email,gpa)
data_set = {name,email,gpa}
print(data_list)
print(data_tuple)
a = {"name":name, "email":email,"GPA":gpa }
print(a)