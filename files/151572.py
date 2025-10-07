name = str(input("Enter your name: "))
email = input("Enter your email: ")
GPA = float(input("Enter your GPA: "))

list_ = [name, email, GPA]
tuple_ = (name, email , GPA)
dict_ = {"name":name,"email":email,"GPA":GPA}

print(list_)
print(tuple_)
print(dict_)