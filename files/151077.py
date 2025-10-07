name = input("Enter your name:")
email = input("Enter your email:")
GPA = input("Enter your GPA:")


data_list  = [name,email,float(GPA)]
data_tuple  = (name,email,float(GPA))
data_dict = {"name" :name,"email":email , "GPA":float(GPA)}
print(data_list)
print(data_tuple)
print(data_dict)