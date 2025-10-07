name = input("Enter your name:")
email = input("Enter your email:")
gpa = float(input("Enter your GPA:"))

data_list = [name,email,gpa]
data_tuple = (name,email,gpa)
data_dict = {'name': name, 'email': email, 'GPA': gpa}

print(data_list)
print(data_tuple)
print(data_dict)