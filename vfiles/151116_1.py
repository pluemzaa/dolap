num1 = input('Enter your name: ')
num2 = input('Enter your email: ')
lang = input('Enter your GPA: ')
num1 = str(num1)
num2 = str(num2)
lang =float(lang)

data_list = [num1, num2, "lang"]
data_tuple = (num1, num2, "lang")
data_dict = {"num1": num1, "num2": num2, "lang": "lang"}
print(data_list)
print(data_tuple)
print(data_dict)