name = input("Enter your name: ")
email = input("Enter your email: ")
gpa = flaot(input("Enter your GPA: "))

data_list = [name,email,gpa]
data_tuple = (name,email,gpa)
data_set = {name,email,gpa}
print(data_list)
print(data_tuple)
print({"name"data_set[0],"email"data_set[1],"GPA"data_set[2]})