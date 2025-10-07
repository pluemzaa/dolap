name = input("Enter your email: ")
gmail = input("Enter your name: ")
gpa = float(input("Enter your GPA: "))

uselist = [gmail,name,gpa]
print(uselist)
usetuple = (gmail,name,gpa)
print(usetuple)
usedict = {'name': name,'email': gmail,'GPA': gpa}
print(usedict)