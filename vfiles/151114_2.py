Name = input('Enter your name:')
Email = input('Enter your email:')
Gpa = input('Enter your GPA:')
gpa = float(Gpa)
data_list = [Name,Email,Gpa]
data_tuple = (Name,Email,Gpa)
data_dict = {"name": Name, "email": Email , "GPA": Gpa}
print(data_list)
print(data_tuple)
print(data_dict)