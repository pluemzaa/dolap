name = input("Enter your name: ")
email = input("Enter your email: ")
gpa = input("Enter your GPA: ")
gpa = float(gpa)

a = [name, email, gpa]
b = (name, email, gpa)
c = {'name': name, 'email': email, 'GPA': gpa}

print(a)
print(b)
print(c)