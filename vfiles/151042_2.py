num1 = input('Enter your name :')
num2 = input('Enter your email :')
lang = input('Enter your GPA:')
num1 = int(num1)
num2 = float(num2)
data_list =[num1, num2 , "lamg"]
data_tuple = (num1, num2 , "lang")
# dctionary
data_dic = {"num" : num1, "num2" : num2 , "lang" : "lang"}
print(data_dic)
print(data_dic['lang'])
print(data_tuple)
print (data_list)