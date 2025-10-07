num1 = input("Enter your name: ")
num2 = input("Enter your email: ")
lang = input("Enter your GPA: ")
lang = float(lang)
data_list =[num1, num2, lang]
data_tutle =(num1, num2, lang)
data_dict ={"name": num1, "email": num2, "GPA": {lang:.2f} }
print(data_list)
print(data_tutle)
print(data_dict)