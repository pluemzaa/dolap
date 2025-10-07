Name = input("Enter your name: ")
Email = input("Enter your email: ")
GPA = input("Enter your GPA: ")
Name = str(Name)
Email = str(Email)
GPA = float(GPA)
a = [Name, Email, GPA]
b = (Name, Email, GPA)
c = {'Name': name, 'Email': Email, 'GPA': GPA}
print(a)
print(b)
print(c)