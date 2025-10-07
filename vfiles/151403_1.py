name = input("Enter your name :")
gmail = input("Enter your email: ")
GPA = float(input("Enter your GPA: "))

data_list = (name, gmail , GPA )
data_tuple = [name, gmail , GPA ]
data_dict = {'name':name,'email':gmail,'GPA':GPA}

print(data_list) 
print(data_tuple)
print(data_dict)