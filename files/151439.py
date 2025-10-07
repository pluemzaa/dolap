name= input("Enter your name:")
email= input("Enter your email:")
GPA = input("Enter your GPA: ")
GPA = float(GPA)

data_list=[name,email,GPA]
data_tuple=(name,email,GPA)
data_Dict={'name':name,'email':email,'GPA':GPA}
print(data_list)
print(data_tuple)
print(data_Dict)