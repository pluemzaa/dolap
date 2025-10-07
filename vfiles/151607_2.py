name=input('Enter your name:')
mail=input('Enter your email:')
gpa=input('Enter your GPA:')
gpa=float(gpa)
data_list=[name,mail,gpa]
data_tuple=(name,mail,gpa)
data_dict={'name':name ,'mail':mail,'gpa':gpa}
print(data_list)
print(data_tuple)
print(data_dict)