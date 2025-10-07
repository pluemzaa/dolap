num1 = input("Enter your name:")
num2 = input("Enter your email:")
lang = float(input("Enter lang:"))
lang = int(lang)
data_list = [num1,num2,lang]
data_tuple = (num1,num2,lang)
data_dict = {"name": num1,"email": num2,"GPA":lang}
print(data_list)
print(data_tuple)
print(data_dict)