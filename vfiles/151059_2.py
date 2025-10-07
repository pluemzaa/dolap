name = input("Enter your name: ")
email = input("Enter your email: ")
gpa = int(input("Enter your GPA: "))
list_ = [name,email,gpa]
tuple_ = (name,email,gpa)
dict_ = {"name":name,"email":email,"GPA":gpa}
print (list_,tuple_,dict_,sep=\n)