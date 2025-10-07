name = input("Enter your name: ")
email = input("Enter your email: ")
gpa = input("Enter your GPA: ")

gpa = float(gpa)

_list = [name, email, gpa]
_dict = (name,email, gpa)
_tuple = {'name': name, 'email': email, 'gpa': gpa}

print(_list)
print(_dict)
print(_tuple)