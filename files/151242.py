name=input("Enter your name:")
email=input("Enter your email:")
gpa=float(input("Enter your GPA:"))

date_list=[name,email,gpa]
date_tuple=(name,email,gpa)
date_Dict={"name": name, "email": email,"gpa": gpa}

print(date_list)
print(date_tuple)
print(date_Dict)