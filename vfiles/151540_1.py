num1 = input('Enter num1 :')
num2 = input('Enter num2 :')
lang = input('Enter lang :')
num1 = int(num1)
num2 = float(num2)
data_list =[num1, num2, "lang"]
data_tuple =(num1, num2, "lang")
#dictionary
data_dict = {"num1" : num1, "num2" : num2, "lang" : lang}
print(data_dict)
print(data_dict['lang'])
print(data_tuple)
print(data_list)