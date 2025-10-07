data_dict = {'name': None, 'email': None, 'GPA': None}
data_dict['name'] = input("Enter your name: ")
data_dict['email'] = input("Enter your email: ")
data_dict['GPA'] = float(input("Enter your GPA: "))

data_list = []
data_list.append(data_dict['name'])
data_list.append(data_dict['email'])
data_list.append(data_dict['GPA'])

print(data_list)
print(tuple(data_list))
print(data_dict)