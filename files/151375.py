num1 = input("Enter your name:")
num2 = input("Enter your email:")
num3  = input("Enter your GPA:")

num3 = float(num3)

lang = "python"
data_list = [num1, num2, num3]
data_tuple = (num1, num2, num3)
data_dict = {"name": num1, "email": num2, "GPA": num3}
print(data_list)
print(data_tuple)
print(data_dict)