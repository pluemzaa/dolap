name = input('Enter your name:')
name = int(name)
email = input('Enter your email:')
email = int(email)
GPA = input("Enter your GPA:")
GPA = float(GPA)

a = [name, email, "GPA"]
b = (name, email, "GPA")
c = {"name" : name , "email" : email, "GPA" : "GPA"}
print(a)
print(b)
print(c)