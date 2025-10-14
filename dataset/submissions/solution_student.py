#student
a = input("Enter your name: ")
b = input("Enter your email: ")
c = input("Enter your GPA: ")


c = float(c)

data_list = [a,b,c]
data_tuple = (a,b,c)
data_dict = {"name":a,"email":b,"GPA":c}
print(data_list)
print(data_tuple)
print(data_dict)