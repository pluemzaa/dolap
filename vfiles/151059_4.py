name = input("Enter your name: ")
email = input("Enter your email: ")
gpa = float(input("Enter your GPA: "))
gpa = gpa:.1f
list_ = [name,email,gpa]
tuple_ = (name,email,gpa)
dict_ = {"name":name,"email":email,"GPA":gpa}
print (list_,tuple_,dict_,sep="\n")