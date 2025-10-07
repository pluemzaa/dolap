name = input("Enter your name: ")
email = input("Enter your email: ")
GPA = input("Enter your GPA: ")
GPA = float(g)
data_list = [name, email, GPA]
data_tuple = [name, email, GPA]
data_dict = {"name": name, "email": email, "g": GPA}

print(data_list)
print(data_tuple)
print(data_dict)