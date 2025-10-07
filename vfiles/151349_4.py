name = input('Enter your name: ')
email = input('Enter your email: ')
gpa = float(input('Enter your GPA: '))
data = "name,email,gpa"
r1 = data.split(",")
data1 = (name,email,gpa)
data2 = {'name': name, 'email':email, 'GPA': gpa }
print(r1)
print(data1)
print(data2)