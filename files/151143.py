name = input("Enter your name:")
email = input("Enter your email:")
gpa = input("Enter your GPA:")
name = str(name)
email = str(email)
gpa = float(gpa)
name_list =[name, email, gpa]
email_tuple = (name, email, gpa)
gpa_dict = {"name" :name, "email" : email, "gpa" : gpa}
print(name_list)
print(email_tuple)
print(gpa_dict)