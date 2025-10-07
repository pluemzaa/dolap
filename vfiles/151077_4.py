name = input("Enter your name: ")
email = input("Enter your email: ")
GPA = input("Enter your GPA: ")


data_list  = [name,email,4.0]
data_tuple  = (name,email,4.0)
data_dict = {"name" : name,"email": email , "GPA": 4.0}

print(data_list)
print(data_tuple)
print(data_dict)