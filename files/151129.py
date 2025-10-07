num1 = input('Enter your name:')
num2 = input('Enter your email:')
lang = input('Enter your GPA:')
#num1 = int(num1)
lang = float(lang)
data_list = [num1,num2,lang]
# data_list[2] = 4.00
data_tuple = (num1,num2,lang)
# dictionary
data_dict ={"name": num1, "email": num2 , "GPA": lang}

print(data_list)
print(data_tuple)
print(data_dict)
# print(data_dict['lang'])