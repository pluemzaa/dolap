#price = input("Enter product price:")
#price = float(price)
#point = 1/500*float(price)
#point = input("Enter your point:")
#Discount = 1/500*float(point)
#print("Discount: %.2f " %Discount)
#total = price-Discount
#print("Total: %.2f Baht" %total)
#pi = 3.14159
#print(f"Pi rounded to 2 decimals: {pi:.2f}") # แสดงค่า pi กำหนดให้แสดงทศนิยม 2 ตำแหน่ง





num1 = input('Enter your name:')
num2 = input('Enter your email:')
lang = input('Enter your GPA:')

lang = float(lang)
data_list = [num1,num2,lang]
data_tuple =(num1,num2,lang)
data_dict ={"name": num1, "email": num2 , "GPA": lang}

print(data_list)
print(data_tuple)
print(data_dict)