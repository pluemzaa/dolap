name = input('Enter your name:')
name = int(name)
email = input('Enter your email:')
email = int(email)
GPA = input("Enter your GPA:")

a = [name, email, "GPA"]
b = (name, email, "GPA")
c = {"num1" : name , "num2" : email, "GPA" : "GPA"}
print(a)
print(b)
print(c)
print(c["num1"],c["GPA"])