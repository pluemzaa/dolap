name = input("Enter your name: ")
email = input("Enter your email: ")
gpa = input("Enter your GPA: ")
gpa = int(gpa)

l = [name, email, gpa]
t = (name, email, gpa)
d = {"name" : name, "email" : email, "GPA" : gpa}

print(l)
print(t)
print(d)