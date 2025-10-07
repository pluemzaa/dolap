name = input('Enter your name:')
email = input('Enter your email:')
gpa = input('Enter your GPA:')
gpa = float(gpa)

data_list = [name, email, gpa]
data_tuple = (name, email, gpa)
data_dict={"name":name, "email": email, "gpa":"gpa"}

print(data_list)
print(data_tuple)
print(data_dict)