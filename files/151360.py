Name = str(input("Enter your name: "))
email = str(input("Enter your email: "))
GPA = float(input("Enter your GPA:"))

Data_list = [Name, email, GPA]
Data_tuple = (Name, email, GPA)
Data_Dict = {"name" : Name, "email" : email, "GPA" : GPA}
print(Data_list)
print(Data_tuple)
print(Data_Dict)