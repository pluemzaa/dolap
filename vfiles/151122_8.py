_name = input("Enter your name: ")
Email_name = input("Enter your email: ")
gpa = input("Enter your GPA: ")
gpa = float(gpa)

data_list = [_name,Email_name,gpa]
data_tuple = (_name,Email_name,gpa)
data_Dict = {'name': _name,'email': Email_name,'GPA': gpa}


print(data_list)
print(data_tuple)
print(data_Dict)