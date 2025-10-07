lang1 = input('Enter your name: ')
lang2 = input('Enter your email: ')
num = input('Enter your GPA: ')
num = float(num)

Data_List =[lang1 , lang2 , num]
Data_List[2] = 4.00
Data_Tuple = (lang1 , lang2 , num)
# dictionary
Data_Dict = {'name': lang1, 'email': lang2, 'GPA': num}
print(Data_List)
print(Data_Tuple)
print(Data_Dict)
print({'name': lang1, 'email': lang2, 'GPA': num})