name = input("Enter your name:")
email = input("Enter your email:")
GPA = input("Enter your GPA:")

List = [name,email,GPA]
Tuple = (name,email,GPA)
Dict = {'name':name,'email':email,'GPA':GPA}
D_1 = "name,email,GPA"
D_1 = D_1.split()
print(List)
print(Tuple)
print(Dict)