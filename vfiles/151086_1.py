name = input("Enter your name: ")
email = input("Enter your email: ")
gpa = float(input("Enter your GPA: "))
data = {'name' : name,'email' : email,'gpa': gpa}
data_list = [name,email,gpa]
data_tuple = (name,email,gpa)
print(data_list)
print(data_tuple)
print(data)