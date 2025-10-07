name = input('Enter your name:')
email = input('Enter your email:')
GPA = input('Enter your GPA:')
GPA = float(GPA)
data_list = [name, email , GPA]
print(data_list)
data_tuple = (name, email , GPA)
print(data_tuple)
data_dict = {"name": name, "email": email , "GPA": GPA}
print(data_dict)