name = input("Enter your name: ")
email = input("Enter your email: ")
gpa = float(input("Enter your GPA: "))

newList = [name, email, gpa]
newTuple = (name, email, gpa)
newDict = {"name":name,"email": email,"GPA": gpa}
print(newList)
print(newTuple)
print(newDict)