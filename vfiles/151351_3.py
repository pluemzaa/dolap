name = input("Enter your name: ")
email = input("Enter your email: ")
gpa = float(input("Enter your GPA: "))

info_list = [name, email, gpa]
info_tuple = (name, email, gpa)
info_dict = {"name": name, "email": email, "GPA": gpa}

print(info_list)
print(info_tuple)
print(info_dict)