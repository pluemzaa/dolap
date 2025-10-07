name = input("Enter your name:")
email = input("Enter your email:")
gpa = input("Enter your GPA:")

gpa= float(gpa)

data_list = [name, email, GPA]
data_tuple = (name, email, GPA)
print(data_list)
print(data_tuple)
data_dict = {"name": name,"email": email, "GPA":gpa}
print(data_dict)