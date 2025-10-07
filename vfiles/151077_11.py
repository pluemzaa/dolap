name = input("Enter your name: ")
email = input("Enter your email: ")
GPA = input("Enter your GPA: ")

data_list  = [name,email,f"{float(GPA):.1f}"]
data_tuple  = (name,email,f"{float(GPA):.1f}")
data_dict = {"name" : name,"email": email , "GPA": f"{float(GPA):.1f}"}

print(data_list)
print(data_tuple)
print(data_dict)